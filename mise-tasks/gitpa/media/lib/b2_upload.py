"""Page-named B2 uploads with cached credentials and content verification."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener
import zipfile


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


OPENER = build_opener(NoRedirect)


def endpoint(url: str) -> str:
    parsed = urlparse(url)
    if (parsed.scheme != 'https' or not parsed.hostname or not parsed.hostname.endswith('.backblazeb2.com')
            or parsed.username or parsed.password or parsed.query or parsed.fragment):
        raise ValueError('Unexpected B2 service endpoint')
    return url.rstrip('/')


def hashes(source: Path) -> tuple[int, str, str]:
    sha1, sha256, size = hashlib.sha1(), hashlib.sha256(), 0
    with source.open('rb') as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b''):
            size += len(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
    if not 0 < size <= 5_000_000_000:
        raise ValueError('File must be nonempty and within the B2 single-upload limit')
    return size, sha1.hexdigest(), sha256.hexdigest()


def asset_name(garden: Path, page: str) -> tuple[str, str]:
    parts = page.split('/')
    if (len(parts) < 4 or 'Asset' not in parts[1:-2]
            or any(not part or part in {'.', '..'} or '___' in part
                   or re.search(r'[\x00-\x1f\x7f<>:"\\|?*]', part) for part in parts)
            or not re.fullmatch('[a-z0-9]+', parts[-1])):
        raise ValueError('Use an existing Owner/Asset/Purpose/format page with valid asset segments')
    path = garden / 'pages' / (page.replace('/', '___') + '.md')
    if not path.is_file() or path.resolve().parent != (garden / 'pages').resolve():
        raise ValueError('Asset page must exist directly in this garden pages directory')
    if not re.search(r'^logseq-entity::\s*\[\[Logseq/Entity/Asset/B2\]\]\s*$', path.read_text(), re.M):
        raise ValueError('Target page must be a Logseq/Entity/Asset/B2 instance')
    return '___'.join(parts[:-1]) + '.' + parts[-1], parts[-1]


def media_type(source: Path, extension: str) -> str:
    if not source.is_file() or source.suffix != '.' + extension:
        raise ValueError('Source extension must match the asset page format')
    with source.open('rb') as file:
        header = file.read(16)
    if not header:
        raise ValueError('Source file is empty')
    signatures = {'gif': (b'GIF87a', b'GIF89a'), 'png': (b'\x89PNG\r\n\x1a\n',),
                  'jpg': (b'\xff\xd8\xff',), 'jpeg': (b'\xff\xd8\xff',), 'pdf': (b'%PDF-',),
                  'mid': (b'MThd',), 'midi': (b'MThd',)}
    if extension in signatures and not header.startswith(signatures[extension]):
        raise ValueError('Source content does not match its asset format')
    if extension in {'mp3', 'wav', 'flac', 'ogg', 'mp4', 'webm'}:
        result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                                 'format=format_name:stream=codec_type,codec_name', '-of', 'json', str(source)],
                                check=True, capture_output=True, text=True)
        info = json.loads(result.stdout)
        formats = info.get('format', {}).get('format_name', '').split(',')
        streams = info.get('streams', [])
        expected = {'mp3': 'mp3', 'wav': 'wav', 'flac': 'flac', 'ogg': 'ogg',
                    'mp4': 'mp4', 'webm': 'webm'}[extension]
        if expected not in formats or not streams:
            raise ValueError('Media format does not match the asset page')
        if extension == 'mp3' and not any(s.get('codec_name') == 'mp3' for s in streams):
            raise ValueError('Prepared MP3 does not contain MP3 audio')
    if extension == 'mfpz':
        with zipfile.ZipFile(source) as archive:
            if not archive.namelist() or sum(x.file_size for x in archive.infolist()) > 64 * 1024 * 1024 or archive.testzip():
                raise ValueError('MicroFreak preset archive is empty, too large or damaged')
        return 'application/octet-stream'
    return {'mid': 'audio/midi', 'midi': 'audio/midi', 'wav': 'audio/wav', 'mp3': 'audio/mpeg'}.get(
        extension, mimetypes.guess_type('asset.' + extension)[0] or 'application/octet-stream')


class B2:
    def __init__(self):
        try:
            key_id, key = os.environ['AWS_ACCESS_KEY_ID'], os.environ['AWS_SECRET_ACCESS_KEY']
            if not key_id or not key:
                raise KeyError('empty credential')
        except KeyError:
            raise ValueError('Missing fnox assets credentials') from None
        basic = base64.b64encode((key_id + ':' + key).encode()).decode()
        auth = self.request('https://api.backblazeb2.com/b2api/v4/b2_authorize_account',
                            headers={'Authorization': 'Basic ' + basic})
        self.token = auth['authorizationToken']
        self.account = auth['accountId']
        storage = auth['apiInfo']['storageApi']
        self.api = endpoint(storage['apiUrl'])
        self.download = endpoint(storage['downloadUrl'])
        self.allowed = storage['allowed']

    def request(self, url, *, headers=None, data=None):
        with OPENER.open(Request(endpoint(url), data=data, headers=headers or {}), timeout=120) as response:
            return json.load(response)

    def call(self, operation, data):
        return self.request(self.api + '/b2api/v4/' + operation,
                            headers={'Authorization': self.token, 'Content-Type': 'application/json'},
                            data=json.dumps(data).encode())

    def bucket(self, requested: str | None, filename: str, verify_only: bool) -> dict:
        allowed = self.allowed.get('buckets')
        if requested is None:
            if not allowed or len(allowed) != 1:
                raise ValueError('Specify --bucket when the key is not restricted to one named bucket')
            requested = allowed[0]['name']
        if allowed and not any(item['name'] == requested for item in allowed):
            raise ValueError('The B2 key does not allow the selected bucket')
        required = {'listBuckets', 'listFiles', 'readFiles'} | (set() if verify_only else {'writeFiles'})
        if not required.issubset(set(self.allowed.get('capabilities', []))):
            raise ValueError('The B2 key lacks required list/read/upload permissions')
        if not filename.startswith(self.allowed.get('namePrefix') or ''):
            raise ValueError('The page-derived filename is outside the B2 key prefix')
        # Bucket-specific lookup also establishes public/private download behavior.
        buckets = self.call('b2_list_buckets', {'accountId': self.account, 'bucketName': requested})['buckets']
        matches = [b for b in buckets if b['bucketName'] == requested]
        if len(matches) != 1:
            raise ValueError('The selected B2 bucket is unavailable to this key')
        return matches[0]

    def current(self, bucket, filename):
        files = self.call('b2_list_file_versions', {'bucketId': bucket['bucketId'],
                          'prefix': filename, 'startFileName': filename, 'maxFileCount': 1})['files']
        return files[0] if files and files[0]['fileName'] == filename else None

    def upload(self, bucket, filename, source, size, sha1, mime):
        target = self.call('b2_get_upload_url', {'bucketId': bucket['bucketId']})
        existing = self.current(bucket, filename)
        if existing:
            check_metadata(existing, filename, size, sha1, mime)
            return existing
        with source.open('rb') as file:
            return self.request(target['uploadUrl'], data=file, headers={
                'Authorization': target['authorizationToken'], 'Content-Length': str(size),
                'X-Bz-File-Name': quote(filename, safe=''), 'X-Bz-Content-Sha1': sha1, 'Content-Type': mime})

    def verify_download(self, url, size, sha256, mime, private):
        headers = {'Authorization': self.token} if private else {}
        digest, received = hashlib.sha256(), 0
        with OPENER.open(Request(endpoint(url), headers=headers), timeout=120) as response:
            if response.status != 200 or response.headers.get('Content-Type', '').split(';')[0] != mime:
                raise ValueError('Downloaded media type or status does not match the prepared file')
            if int(response.headers.get('Content-Length', '-1')) != size:
                raise ValueError('Downloaded length differs from the prepared file')
            while chunk := response.read(1024 * 1024):
                digest.update(chunk)
                received += len(chunk)
                if received > size:
                    raise ValueError('Download exceeds the prepared file length')
        if received != size or digest.hexdigest() != sha256:
            raise ValueError('Downloaded SHA-256 differs from the prepared file')


def check_metadata(info, filename, size, sha1, mime):
    if (info.get('action') != 'upload' or info.get('fileName') != filename or info.get('contentLength') != size
            or info.get('contentSha1') != sha1 or info.get('contentType') != mime):
        raise ValueError('Destination exists with conflicting content, visibility or media metadata')


def transfer(source: Path, garden: Path, page: str, requested_bucket=None, verify_only=False, client=None) -> str:
    filename, extension = asset_name(garden, page)
    mime = media_type(source, extension)
    size, sha1, sha256 = hashes(source)
    client = client or B2()
    bucket = client.bucket(requested_bucket, filename, verify_only)
    current = client.current(bucket, filename)
    if current:
        check_metadata(current, filename, size, sha1, mime)
    else:
        if verify_only:
            raise ValueError('Object is absent; --verify-only does not upload')
        # Check again after obtaining authorization; conflicting versions stay untouched.
        info = client.upload(bucket, filename, source, size, sha1, mime)
        check_metadata(info, filename, size, sha1, mime)
    if hashes(source) != (size, sha1, sha256):
        raise ValueError('Source changed during transfer')
    url = client.download + '/file/' + quote(bucket['bucketName'], safe='') + '/' + quote(filename, safe='')
    client.verify_download(url, size, sha256, mime, bucket['bucketType'] != 'allPublic')
    print('Verified existing object' if current else 'Uploaded and verified object')
    if bucket['bucketType'] != 'allPublic':
        print('Private object: downloads require garden B2 authentication')
    return url


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('page')
    parser.add_argument('--garden', type=Path, required=True)
    parser.add_argument('--bucket')
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    try:
        print(transfer(args.source, args.garden, args.page, args.bucket, args.verify_only))
    except HTTPError as error:
        parser.exit(1, f'error: B2 HTTP {error.code}; check access and retry after resolving the failure\n')
    except ValueError as error:
        parser.exit(1, f'error: {error}\n')
    except (URLError, OSError, KeyError, zipfile.BadZipFile, subprocess.CalledProcessError):
        # Provider responses and subprocess stderr can contain sensitive context.
        parser.exit(1, 'error: asset validation or B2 transfer failed; no verified URL produced\n')


if __name__ == '__main__':
    main()
