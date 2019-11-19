# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client import api
from exmail.client.base import BaseClient
from exmail.storage.cache import EmailCache


class SecretClient(BaseClient):

    user = api.User()
    department = api.Department()
    tag = api.Tag()
    group = api.Group()
    log = api.Log()
    mail = api.Mail()
    option = api.Option()
    service = api.Service()

    def __init__(self, corp_id, corp_secret, prefix='client', storage=None, timeout=None, auto_retry=True):
        super(SecretClient, self).__init__(storage, timeout, auto_retry)
        self.corp_id = corp_id
        self.corp_secret = corp_secret
        self.cache = EmailCache(self.storage, prefix)

    @property
    def access_token(self):
        token = self.cache.access_token.get()
        if token is None:
            ret = self.get_access_token()
            token = ret['access_token']
            expires_in = ret.get('expires_in', 7200)
            self.cache.access_token.set(value=token, ttl=expires_in)
        return token

    def _handle_pre_request(self, method, uri, kwargs):
        if 'access_token=' in uri or 'access_token' in kwargs.get('params', {}):
            raise ValueError("uri参数中不允许有access_token: " + uri)
        uri = '%s%saccess_token=%s' % (uri, '&' if '?' in uri else '?', self.access_token)
        return method, uri, kwargs

    def _handle_request_except(self, e, func, *args, **kwargs):
        # 可根据状态码重试
        if e.errcode in tuple():
            self.cache.access_token.delete()
            if self.auto_retry:
                return func(*args, **kwargs)
        raise e

    def get_access_token(self):
        return self._request(
            'GET',
            '/gettoken',
            params={'corpid': self.corp_id, 'corpsecret': self.corp_secret}
        )

