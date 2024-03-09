import io
import json
import os
import zipfile as zf
from collections import namedtuple
from pathlib import Path
from struct import Struct

from biolib import utils, api
from biolib._internal.http_client import HttpClient
from biolib.app import BioLibApp
from biolib.biolib_api_client.biolib_account_api import BiolibAccountApi
from biolib.biolib_api_client import BiolibApiClient
from biolib.biolib_api_client.lfs_types import LargeFileSystem, LargeFileSystemVersion
from biolib.biolib_logging import logger
from biolib.biolib_errors import BioLibError
from biolib.typing_utils import List, Tuple, Iterator, Optional
from biolib.utils.app_uri import parse_app_uri
from biolib.utils.zip.remote_zip import RemoteZip  # type:ignore


def _get_lfs_info_from_uri(lfs_uri):
    lfs_uri_parts = lfs_uri.split('/')
    lfs_uri_parts = [uri_part for uri_part in lfs_uri_parts if '@' not in uri_part]  # Remove hostname
    team_account_handle = lfs_uri_parts[0]
    lfs_name = lfs_uri_parts[1]
    account = BiolibAccountApi.fetch_by_handle(team_account_handle)
    return account, lfs_name


def get_files_and_size_of_directory(directory: str) -> Tuple[List[str], int]:
    data_size = 0
    file_list: List[str] = []

    for path, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(path, file)
            if os.path.islink(file_path):
                continue  # skip symlinks

            relative_file_path = file_path[len(directory) + 1:]  # +1 to remove starting slash
            file_list.append(relative_file_path)
            data_size += os.path.getsize(file_path)

    return file_list, data_size


def get_iterable_zip_stream(files: List[str], chunk_size: int) -> Iterator[bytes]:
    class ChunkedIOBuffer(io.RawIOBase):
        def __init__(self, chunk_size: int):
            super().__init__()
            self.chunk_size = chunk_size
            self.tmp_data = bytearray()

        def get_buffer_size(self):
            return len(self.tmp_data)

        def read_chunk(self):
            chunk = bytes(self.tmp_data[:self.chunk_size])
            self.tmp_data = self.tmp_data[self.chunk_size:]
            return chunk

        def write(self, data):
            data_length = len(data)
            self.tmp_data += data
            return data_length

    # create chunked buffer to hold data temporarily
    io_buffer = ChunkedIOBuffer(chunk_size)

    # create zip writer that will write to the io buffer
    zip_writer = zf.ZipFile(io_buffer, mode='w')  # type: ignore

    for file_path in files:
        # generate zip info and prepare zip pointer for writing
        z_info = zf.ZipInfo.from_file(file_path)
        zip_pointer = zip_writer.open(z_info, mode='w')
        if Path(file_path).is_file():
            # read file chunk by chunk
            with open(file_path, 'br') as file_pointer:
                while True:
                    chunk = file_pointer.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    # write the chunk to the zip
                    zip_pointer.write(chunk)
                    # if writing the chunk caused us to go over chunk_size, flush it
                    if io_buffer.get_buffer_size() > chunk_size:
                        yield io_buffer.read_chunk()

        zip_pointer.close()

    # flush any remaining data in the stream (e.g. zip file meta data)
    zip_writer.close()
    while True:
        chunk = io_buffer.read_chunk()
        if len(chunk) == 0:
            break
        yield chunk


def create_large_file_system(lfs_uri: str) -> str:
    BiolibApiClient.assert_is_signed_in(authenticated_action_description='create a Large File System')

    uri_parsed = parse_app_uri(lfs_uri)
    response = api.client.post(
        path='/lfs/',
        data={
            'account_handle': uri_parsed['account_handle_normalized'],
            'name': uri_parsed['app_name'],
        },
    )
    lfs: LargeFileSystem = response.json()
    logger.info(f"Successfully created new Large File System '{lfs['uri']}'")
    return lfs['uri']


def push_large_file_system(lfs_uri: str, input_dir: str, chunk_size_in_mb: Optional[int] = None) -> str:
    BiolibApiClient.assert_is_signed_in(authenticated_action_description='push data to a Large File System')

    if not os.path.isdir(input_dir):
        raise BioLibError(f'Could not find folder at {input_dir}')

    if os.path.realpath(input_dir) == '/':
        raise BioLibError('Pushing your root directory is not possible')

    original_working_dir = os.getcwd()
    os.chdir(input_dir)
    files_to_zip, data_size_in_bytes = get_files_and_size_of_directory(directory=os.getcwd())

    if data_size_in_bytes > 4_500_000_000_000:
        raise BioLibError('Attempted to push directory with a size larger than the limit of 4.5 TB')

    min_chunk_size_bytes = 10_000_000
    chunk_size_in_bytes: int
    if chunk_size_in_mb:
        chunk_size_in_bytes = chunk_size_in_mb * 1_000_000  # Convert megabytes to bytes
        if chunk_size_in_bytes < min_chunk_size_bytes:
            logger.warning('Specified chunk size is too small, using minimum of 10 MB instead.')
            chunk_size_in_bytes = min_chunk_size_bytes
    else:
        # Calculate chunk size based on max chunk count of 10_000, using 9_000 to be on the safe side
        chunk_size_in_bytes = max(min_chunk_size_bytes, int(data_size_in_bytes / 9_000))

    data_size_in_mb = round(data_size_in_bytes / 10 ** 6)
    print(f'Zipping {len(files_to_zip)} files, in total ~{data_size_in_mb}mb of data')

    response = api.client.post(path='/lfs/versions/', data={'resource_uri': lfs_uri})
    lfs_version: LargeFileSystemVersion = response.json()
    iterable_zip_stream = get_iterable_zip_stream(files=files_to_zip, chunk_size=chunk_size_in_bytes)

    multipart_uploader = utils.MultiPartUploader(
        use_process_pool=True,
        get_presigned_upload_url_request=dict(
            headers=None,
            requires_biolib_auth=True,
            path=f"/lfs/versions/{lfs_version['uuid']}/presigned_upload_url/",
        ),
        complete_upload_request=dict(
            headers=None,
            requires_biolib_auth=True,
            path=f"/lfs/versions/{lfs_version['uuid']}/complete_upload/",
        ),
    )

    multipart_uploader.upload(payload_iterator=iterable_zip_stream, payload_size_in_bytes=data_size_in_bytes)
    os.chdir(original_working_dir)
    logger.info(f"Successfully pushed a new LFS version '{lfs_version['uri']}'")
    return lfs_version['uri']


def describe_large_file_system(lfs_uri: str, output_as_json: bool = False) -> None:
    BiolibApiClient.assert_is_signed_in(authenticated_action_description='describe a Large File System')
    lfs_resource = BioLibApp(lfs_uri)
    response = api.client.get(path=f"/lfs/versions/{lfs_resource.version['public_id']}/")
    lfs_version: LargeFileSystemVersion = response.json()

    files = []
    total_size = 0
    with RemoteZip(url=lfs_version['presigned_download_url']) as remote_zip:
        central_directory = remote_zip.get_central_directory()
        for file in central_directory.values():
            files.append(dict(path=file['filename'], size_bytes=file['file_size']))
            total_size += file['file_size']

    lfs_version_metadata = dict(files=files, **lfs_version)
    lfs_version_metadata['size_bytes'] = total_size

    if output_as_json:
        print(json.dumps(lfs_version_metadata, indent=4))
    else:
        print(f"Large File System {lfs_version_metadata['uri']}\ntotal {lfs_version_metadata['size_bytes']} bytes\n")
        print('size bytes    path')
        for file in files:
            size_string = str(file['size_bytes'])
            leading_space_string = ' ' * (10 - len(size_string))
            print(f"{leading_space_string}{size_string}    {file['path']}")


def get_file_data_from_large_file_system(lfs_uri: str, file_path: str) -> bytes:
    BiolibApiClient.assert_is_signed_in(authenticated_action_description='get file from a Large File System')
    lfs_resource = BioLibApp(lfs_uri)
    response = api.client.get(path=f"/lfs/versions/{lfs_resource.version['public_id']}/")
    lfs_version: LargeFileSystemVersion = response.json()
    lfs_url = lfs_version['presigned_download_url']

    with RemoteZip(lfs_url) as remote_zip:
        central_directory = remote_zip.get_central_directory()
        if file_path not in central_directory:
            raise Exception('File not found in Large File System')

        file_info = central_directory[file_path]

        local_file_header_signature_bytes = b'\x50\x4b\x03\x04'
        local_file_header_struct = Struct('<H2sHHHIIIHH')
        LocalFileHeader = namedtuple('LocalFileHeader', (
            'version',
            'flags',
            'compression_raw',
            'mod_time',
            'mod_date',
            'crc_32_expected',
            'compressed_size_raw',
            'uncompressed_size_raw',
            'file_name_len',
            'extra_field_len',
        ))

        local_file_header_start = file_info['header_offset'] + len(local_file_header_signature_bytes)
        local_file_header_end = local_file_header_start + local_file_header_struct.size

        local_file_header_response = HttpClient.request(
            url=lfs_url,
            headers={'range': f'bytes={local_file_header_start}-{local_file_header_end - 1}'},
            timeout_in_seconds=300,
        )
        local_file_header = LocalFileHeader._make(local_file_header_struct.unpack(local_file_header_response.content))

        file_start = local_file_header_end + local_file_header.file_name_len + local_file_header.extra_field_len
        file_end = file_start + file_info['file_size']

        response = HttpClient.request(
            url=lfs_url,
            headers={'range': f'bytes={file_start}-{file_end - 1}'},
            timeout_in_seconds=300,  # timeout after 5 min
        )
        return response.content
