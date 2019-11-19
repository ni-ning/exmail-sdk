# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json

from exmail.storage import BaseStorage
from exmail.core.utils import to_text


class KvStorage(BaseStorage):
    def __init__(self, kvdb, prefix='exmail'):
        for method_name in ('get', 'set', 'delete'):
            assert hasattr(kvdb, method_name)
        self.kvdb = kvdb
        self.prefix = prefix

    def key_name(self, key):
        return '{0}:{1}'.format(self.prefix, key)

    def get(self, key, default=None):
        key = self.key_name(key)
        value = self.kvdb.get(key)
        if value is None:
            return default
        return json.loads(to_text(value))

    def set(self, key, value, ttl=None):
        if value is None:
            return
        key = self.key_name(key)
        value = json.dumps(value)
        self.kvdb.set(key, value, ttl)

    def delete(self, key):
        key = self.key_name(key)
        self.kvdb.delete(key)
