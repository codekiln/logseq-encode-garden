import hashlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from b2_upload import B2, asset_name, check_metadata, endpoint, media_type, transfer


class Response(io.BytesIO):
    status = 200
    def __init__(self, body, mime='image/gif', size=None):
        super().__init__(body)
        self.headers = {'Content-Type': mime, 'Content-Length': str(len(body) if size is None else size)}


class FakeB2:
    download = 'https://f005.backblazeb2.com'
    def __init__(self, current=None):
        self.info = current
        self.uploads = 0
        self.verified = False
    def bucket(self, requested, filename, verify_only):
        return {'bucketName': 'garden', 'bucketId': 'bucket-id', 'bucketType': 'allPublic'}
    def current(self, bucket, filename):
        return self.info
    def upload(self, bucket, filename, source, size, sha1, mime):
        self.uploads += 1
        return {'action': 'upload', 'fileName': filename, 'contentLength': size,
                'contentSha1': sha1, 'contentType': mime}
    def verify_download(self, *args):
        self.verified = True


class MediaUploadTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'pages').mkdir()
        self.page = 'Course with Spaces/Asset/Diagram/Overview/gif'
        self.page_path = self.root / 'pages' / (self.page.replace('/', '___') + '.md')
        self.page_path.write_text('tags:: [[Existing]]\nlogseq-entity:: [[Logseq/Entity/Asset/B2]]\n- # Diagram\n')
        self.source = self.root / 'prepared.gif'
        self.source.write_bytes(b'GIF89a' + b'example')
        self.filename = 'Course with Spaces___Asset___Diagram___Overview.gif'
        self.info = {'action': 'upload', 'fileName': self.filename,
                     'contentLength': self.source.stat().st_size,
                     'contentSha1': hashlib.sha1(self.source.read_bytes()).hexdigest(), 'contentType': 'image/gif'}

    def test_additive_asset_entity_markers_are_accepted(self):
        self.page_path.write_text('tags:: [[Existing]]\nlogseq-entity:: [[Logseq/Entity/Asset/B2]], [[Logseq/Entity/Other]]\n- # Diagram\n')
        self.assertEqual(asset_name(self.root, self.page), (self.filename, 'gif'))

    def test_body_entity_marker_does_not_establish_asset_type(self):
        for body in ('- # Diagram\nlogseq-entity:: [[Logseq/Entity/Asset/B2]]\n',
                     '\nlogseq-entity:: [[Logseq/Entity/Asset/B2]]\n'):
            with self.subTest(body=body):
                self.page_path.write_text('tags:: [[Existing]]\nlogseq-entity:: [[Logseq/Entity/Other]]\n' + body)
                with self.assertRaises(ValueError):
                    asset_name(self.root, self.page)

    def test_idempotent_existing_object_keeps_page_and_uploads_unchanged(self):
        client = FakeB2(self.info)
        original = self.page_path.read_bytes()
        url = transfer(self.source, self.root, self.page, client=client)
        self.assertIn('Course%20with%20Spaces___Asset', url)
        self.assertEqual(client.uploads, 0)
        self.assertTrue(client.verified)
        self.assertEqual(self.page_path.read_bytes(), original)

    def test_public_object_uses_discovered_s3_endpoint_and_verifies_download(self):
        client = FakeB2(self.info)
        client.s3 = 'https://s3.us-east-005.backblazeb2.com'
        url = transfer(self.source, self.root, self.page, client=client)
        self.assertEqual(url, client.s3 + '/garden/Course%20with%20Spaces___Asset___Diagram___Overview.gif')
        self.assertTrue(client.verified)
        self.assertEqual(client.uploads, 0)

    def test_discovered_s3_endpoint_rejects_untrusted_hosts(self):
        auth = {'authorizationToken': 'synthetic-token', 'accountId': 'synthetic-account',
                'apiInfo': {'storageApi': {'apiUrl': 'https://api005.backblazeb2.com',
                            'downloadUrl': 'https://f005.backblazeb2.com',
                            's3ApiUrl': 'https://untrusted.example', 'allowed': {}}}}
        with patch.dict('os.environ', {'AWS_ACCESS_KEY_ID': 'synthetic-key-id',
                                      'AWS_SECRET_ACCESS_KEY': 'synthetic-key'}), patch.object(
                B2, 'request', return_value=auth):
            with self.assertRaises(ValueError):
                B2()

    def test_private_object_keeps_authenticated_native_download_endpoint(self):
        client = FakeB2(self.info)
        client.s3 = 'https://s3.us-east-005.backblazeb2.com'
        client.bucket = lambda *args: {'bucketName': 'garden', 'bucketType': 'allPrivate'}
        url = transfer(self.source, self.root, self.page, client=client)
        self.assertTrue(url.startswith(client.download + '/file/garden/'))
        self.assertTrue(client.verified)

    def test_conflicting_or_hidden_destination_is_never_uploaded(self):
        for change in [{'contentSha1': 'different'}, {'contentType': 'text/plain'}, {'action': 'hide'}]:
            with self.subTest(change=change):
                client = FakeB2(self.info | change)
                with self.assertRaises(ValueError):
                    transfer(self.source, self.root, self.page, client=client)
                self.assertEqual(client.uploads, 0)
                self.assertFalse(client.verified)

    def test_verify_only_absent_object_does_not_upload(self):
        client = FakeB2()
        with self.assertRaises(ValueError):
            transfer(self.source, self.root, self.page, verify_only=True, client=client)
        self.assertEqual(client.uploads, 0)

    def test_new_object_must_pass_full_download_verification(self):
        client = FakeB2()
        with patch.object(client, 'verify_download', side_effect=ValueError('download mismatch')):
            with self.assertRaises(ValueError):
                transfer(self.source, self.root, self.page, client=client)
        self.assertEqual(client.uploads, 1)

    def test_invalid_names_pages_and_formats_stop_before_network(self):
        for name in ['../Asset/Diagram/gif', 'Course/Asset/a___b/gif', 'Course/Asset/Bad:Name/gif',
                     'Course//Asset/Diagram/gif', 'Course/Asset/Diagram/GIF']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                asset_name(self.root, name)
        self.page_path.unlink()
        with self.assertRaises(ValueError):
            asset_name(self.root, self.page)
        self.source.write_bytes(b'not a GIF')
        with self.assertRaises(ValueError):
            media_type(self.source, 'gif')

    def test_presets_and_midi_have_correct_media_types(self):
        preset = self.root / 'prepared.mfpz'
        with zipfile.ZipFile(preset, 'w') as archive:
            archive.writestr('0_preset', 'disposable preset fixture')
        self.assertEqual(media_type(preset, 'mfpz'), 'application/octet-stream')
        midi = self.root / 'prepared.mid'
        midi.write_bytes(b'MThd\x00\x00\x00\x06\x00\x00\x00\x01\x00\x60')
        self.assertEqual(media_type(midi, 'mid'), 'audio/midi')

    def test_mp3_requires_real_mp3_codec(self):
        mp3 = self.root / 'prepared.mp3'
        mp3.write_bytes(b'fake mp3')
        with patch('b2_upload.subprocess.run') as probe:
            probe.return_value.stdout = '{"format":{"format_name":"mp3"},"streams":[{"codec_name":"aac"}]}'
            with self.assertRaises(ValueError):
                media_type(mp3, 'mp3')

    def test_bucket_and_prefix_restrictions_enforced_before_lookup(self):
        client = object.__new__(B2)
        client.allowed = {'buckets': [{'id': 'bucket-id', 'name': 'garden'}],
                          'capabilities': ['listBuckets', 'listFiles', 'readFiles', 'writeFiles'], 'namePrefix': 'Course___'}
        with patch.object(client, 'call') as call:
            with self.assertRaises(ValueError):
                client.bucket('other-garden', 'Course___Asset.gif', False)
            with self.assertRaises(ValueError):
                client.bucket(None, 'Wrong___Asset.gif', False)
            call.assert_not_called()
        client.allowed['buckets'] = None
        with self.assertRaises(ValueError):
            client.bucket(None, 'Course___Asset.gif', False)

    def test_download_rejects_wrong_type_length_or_same_size_content(self):
        client = object.__new__(B2)
        body = b'GIF89aexample'
        checksum = hashlib.sha256(body).hexdigest()
        for response in [Response(body, 'text/plain'), Response(body, size=99), Response(b'GIF89awrong!!')]:
            with self.subTest(response=response), patch('b2_upload.OPENER.open', return_value=response):
                with self.assertRaises(ValueError):
                    client.verify_download('https://f005.backblazeb2.com/file/garden/file.gif', len(body), checksum, 'image/gif', False)

    def test_endpoint_accepts_b2_api_download_and_upload_hosts(self):
        for url in ['https://api005.backblazeb2.com', 'https://f005.backblazeb2.com/file/garden/a.mp3',
                    'https://pod-050-1046-09.backblaze.com/b2api/v4/b2_upload_file/bucket/token']:
            with self.subTest(url=url):
                self.assertEqual(endpoint(url), url)
        for url in ['http://api005.backblazeb2.com', 'https://example.com', 'https://evilbackblaze.com',
                    'https://user:pw@pod-1.backblaze.com', 'https://pod-1.backblaze.com/x?y=1']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                endpoint(url)


if __name__ == '__main__':
    unittest.main()
