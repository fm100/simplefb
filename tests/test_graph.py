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
        url_params = urllib.parse.urlencode({
            'access_token': 'test-token',
            'fields': 'id,name'
        })
        url = 'https://graph.facebook.com/me?%s' % url_params
        data = b'{"id": "1234", "name": "Freddie"}'
        mock_urlopen.return_value = io.BytesIO(data)
        result = simplefb.me('test-token', ver='v2.4')
        self.assertEqual('1234', result['id'])
        self.assertEqual('Freddie', result['name'])
        mock_request.assert_called_once_with(url=url, data=None, method='GET')

    @patch('urllib.request.urlopen')
    @patch('urllib.request.Request')
    def test_me_fields(self, mock_request, mock_urlopen):
        url_params = urllib.parse.urlencode({
            'access_token': 'test-token',
            'fields': 'id,name,gender'
        })
        url = 'https://graph.facebook.com/me?%s' % url_params
        data = b'{"id": "1234", "name": "Freddie", "gender": "male"}'
        mock_urlopen.return_value = io.BytesIO(data)
        result = simplefb.me('test-token',
                             fields=['id', 'name', 'gender'],
                             ver='v2.4')
        self.assertEqual('1234', result['id'])
        self.assertEqual('Freddie', result['name'])
        self.assertEqual('male', result['gender'])
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
            short_lived_token='test-token',
            ver='v2.4'
        )
        self.assertEqual('long-token', result['access_token'][0])
        self.assertEqual('10000', result['expires'][0])
        mock_request.assert_called_once_with(url=url, data=None, method='GET')
