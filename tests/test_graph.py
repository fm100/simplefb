# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
import urllib.request
import urllib.parse
import io

import simplefb


class TestGraph(unittest.TestCase):
    @patch('urllib.request.urlopen')
    @patch('urllib.request.Request')
    def test_me(self, mock_request, mock_urlopen):
        url = 'https://graph.facebook.com/me?access_token=test-token'
        data = b'{"name": "Freddie", "id": "1234"}'
        mock_urlopen.return_value = io.BytesIO(data)
        result = simplefb.me('test-token')
        self.assertEqual('1234', result['id'])
        self.assertEqual('Freddie', result['name'])
        mock_request.assert_called_once_with(url=url, data=None, method='GET')

    @patch('urllib.request.urlopen')
    @patch('urllib.request.Request')
    def test_fb_exchange_token(self, mock_request, mock_urlopen):
        url_params = urllib.parse.urlencode({
            'grant_type': 'fb_exchange_token',
            'client_id': 'app-id',
            'client_secret': 'app-secret',
            'fb_exchange_token': 'test-token',
        })
        url = 'https://graph.facebook.com/oauth/access_token?%s' % url_params
        data = b'access_token=long-token&expires=10000'
        mock_urlopen.return_value = io.BytesIO(data)
        result = simplefb.fb_exchange_token(
            app_id='app-id',
            app_secret='app-secret',
            short_lived_token='test-token'
        )
        self.assertEqual('long-token', result['access_token'][0])
        self.assertEqual('10000', result['expires'][0])
        mock_request.assert_called_once_with(url=url, data=None, method='GET')
