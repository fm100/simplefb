import asyncio
import io
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

import simplefb


class TestGraph(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_me(self, mock_urlopen):
        data = b'{"id": "1234", "name": "Freddie"}'
        mock_urlopen.return_value = io.BytesIO(data)
        result = simplefb.me('test-token')
        self.assertEqual('1234', result['id'])
        self.assertEqual('Freddie', result['name'])

    @patch('urllib.request.urlopen')
    def test_me_fields(self, mock_urlopen):
        data = b'{"id": "1234", "name": "Freddie", "gender": "male"}'
        mock_urlopen.return_value = io.BytesIO(data)
        result = simplefb.me('test-token',
                             fields=['id', 'name', 'gender'])
        self.assertEqual('1234', result['id'])
        self.assertEqual('Freddie', result['name'])
        self.assertEqual('male', result['gender'])

    @patch('urllib.request.urlopen')
    def test_fb_exchange_token(self, mock_urlopen):
        data = b'access_token=long-token&expires=10000'
        mock_urlopen.return_value = io.BytesIO(data)
        result = simplefb.fb_exchange_token(
            app_id='app-id',
            app_secret='app-secret',
            short_lived_token='test-token'
        )
        self.assertEqual('long-token', result['access_token'][0])
        self.assertEqual('10000', result['expires'][0])


class TestGraphAsync(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()

    def run_coroutine(self, coroutine):
        return self.loop.run_until_complete(coroutine)

    @patch('aiohttp.ClientSession.get')
    def test_me_async(self, mock_session_get):
        async def text():
            return '{"id": "1234", "name": "Freddie"}'

        mock_response = MagicMock()
        mock_response.text.return_value = text()
        mock_session_get.return_value = mock_response

        result = self.run_coroutine(simplefb.me_async('test-token'))
        self.assertEqual('1234', result['id'])
        self.assertEqual('Freddie', result['name'])

    @patch('aiohttp.ClientSession.get')
    def test_me_fields_async(self, mock_session_get):
        async def text():
            return '{"id": "1234", "name": "Freddie", "gender": "male"}'

        mock_response = MagicMock()
        mock_response.text.return_value = text()
        mock_session_get.return_value = mock_response

        result = self.run_coroutine(
            simplefb.me_async('test-token',
                              fields=['id', 'name', 'gender'])
        )
        self.assertEqual('1234', result['id'])
        self.assertEqual('Freddie', result['name'])
        self.assertEqual('male', result['gender'])

    @patch('aiohttp.ClientSession.get')
    def test_fb_exchange_token_async(self, mock_session_get):
        async def text():
            return 'access_token=long-token&expires=10000'

        mock_response = MagicMock()
        mock_response.text.return_value = text()
        mock_session_get.return_value = mock_response

        result = self.run_coroutine(
            simplefb.fb_exchange_token_async(
                app_id='app-id',
                app_secret='app-secret',
                short_lived_token='test-token'
            )
        )
        self.assertEqual('long-token', result['access_token'][0])
        self.assertEqual('10000', result['expires'][0])
