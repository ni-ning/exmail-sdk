# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import inspect
import logging
import requests
import json

from exmail.client.api.base import EmailBaseAPI
from exmail.storage.memorystorage import MemoryStorage
from exmail.core.exceptions import EmailClientException

logger = logging.getLogger(__name__)


def _is_api_endpoint(obj):
    return isinstance(obj, EmailBaseAPI)


class BaseClient(object):
    _http = requests.Session()

    API_BASE_URL = 'https://api.exmail.qq.com/cgi-bin'

    def __new__(cls, *args, **kwargs):
        self = super(BaseClient, cls).__new__(cls)
        api_endpoints = inspect.getmembers(self, _is_api_endpoint)
        for name, api in api_endpoints:
            api_cls = type(api)
            api = api_cls(self)
            setattr(self, name, api)
        return self

    def __init__(self, storage=None, timeout=None, auto_retry=True):
        self.storage = storage or MemoryStorage()
        self.timeout = timeout
        self.auto_retry = auto_retry

    def _request(self, method, url_or_endpoint, **kwargs):
        if not url_or_endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = "%s%s" % (api_base_url, url_or_endpoint)
        else:
            url = url_or_endpoint

        if 'params' not in kwargs:
            kwargs['params'] = {}
        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(kwargs['data'], ensure_ascii=False)
            body = body.encode('utf-8')
            kwargs['data'] = body
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

        try:
            res.raise_for_status()
        except requests.RequestException as e:
            logger.error('\n【请求方法和地址】: %s %s'
                         '\n【请求参数】: params %s, data: %s'
                         '\n【异常信息】: %s' % (method, url,
                                           kwargs.get('params', ''), kwargs.get('data', ''), str(e)))

            raise EmailClientException(
                errcode=None,
                errmsg=None,
                client=self,
                request=e.request,
                response=e.response)

        result = self._handle_result(
            res, method, url, result_processor, **kwargs
        )
        logger.debug("\n【请求地址】: %s\n【请求参数】：%s \n%s\n【响应数据】：%s",
                     url, kwargs.get('params', ''), kwargs.get('data', ''), result)

        return result

    def _handle_result(self, res, method=None, url=None, result_processor=None, **kwargs):
        if not isinstance(res, dict):
            result = res.json()
        else:
            result = res
        if not isinstance(result, dict):
            return result

        if 'errcode' in result:
            result['errcode'] = int(result['errcode'])
        if 'errcode' in result and result['errcode'] != 0:
            errcode = result['errcode']
            errmsg = result.get('errmsg', errcode)
            logger.error('\n【请求方法和地址】: %s %s'
                         '\n【请求参数】: params %s, data: %s'
                         '\n【异常信息】: %s' % (method, url,
                                           kwargs.get('params', ''), kwargs.get('data', ''), result))
            raise EmailClientException(errcode,
                                       errmsg,
                                       client=self,
                                       request=res.request,
                                       response=res)

        return result if not result_processor else result_processor(result)

    def _handle_pre_request(self, method, uri, kwargs):
        return method, uri, kwargs

    def _handle_request_except(self, e, func, *args, **kwargs):
        raise e

    def request(self, method, uri, **kwargs):
        method, uri_with_access_token, kwargs = self._handle_pre_request(method, uri, kwargs)
        try:
            return self._request(method, uri_with_access_token, **kwargs)
        except EmailClientException as e:
            return self._handle_request_except(e, self.request, method, uri, **kwargs)

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
