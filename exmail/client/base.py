# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
import requests
import json
from six.moves.urllib.parse import urljoin

from exmail.storage.memorystorage import MemoryStorage


logger = logging.getLogger(__name__)


class BaseClient(object):

    _http = requests.Session()

    API_BASE_URL = 'https://api.exmail.qq.com/cgi-bin'

    def __init__(self, storage=None, timeout=None, auto_retry=True):
        self.storage = storage or MemoryStorage()
        self.timeout = timeout
        self.auto_retry = auto_retry

    def _request(self, method, url_or_endpoint, **kwargs):
        if not url_or_endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = urljoin(api_base_url, url_or_endpoint)
        else:
            url = url_or_endpoint
        if 'params' not in kwargs:
            kwargs['params'] = {}
        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(kwargs['data'], ensure_ascii=False)
            body = body.encode('utf-8')
            kwargs['body'] = body
            if 'headers' not in kwargs:
                kwargs['headers'] = {}
            kwargs['headers']['Content-Type'] = 'application/json'

        kwargs['timeout'] = kwargs.get('timeout', self.timeout)
        result_processor = kwargs.pop('result_processor', None)
        res = self._http.request(
            method=method,
            url=url,
            **kwargs
        )

        result = self._handle_result(
            res, method, url, result_processor, **kwargs
        )
        try:
            res.raise_for_status()
        except requests.RequestException as reqe:
            logger.error('')

        return result

    def _handle_result(self, res, method=None, url=None, result_processor=None, **kwargs):
        return res

    def request(self, method, uri, **kwargs):
        return self._request(method, uri, **kwargs)

    def get(self, uri, params=None, **kwargs):
        """
        get 接口请求

        :param uri: 请求url
        :param params: get 参数（dict 格式）
        """
        if params is not None:
            kwargs['params'] = params
        return self.request('GET', uri, **kwargs)

    def post(self, uri, data=None, params=None, **kwargs):
        """
        post 接口请求

        :param uri: 请求url
        :param data: post 数据（dict 格式会自动转换为json）
        :param params: post接口中url问号后参数（dict 格式）
        """
        if data is not None:
            kwargs['data'] = data
        if params is not None:
            kwargs['params'] = params
        return self.request('POST', uri, **kwargs)
