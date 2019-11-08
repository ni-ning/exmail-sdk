# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest


class StorageTestCase(unittest.TestCase):
    def test_email_cache(self, storage=None):
        from exmail.storage.cache import EmailCache
        if storage is None:
            return
        cache = EmailCache(storage)
        cache.access_token.set('corp', 'test1', 7200)
        self.assertEqual('test1', cache.access_token.get('corp'))

    def test_caches(self, storage=None):
        if storage is None:
            return
        self.test_email_cache(storage)

    def test_memory_storage(self):
        from exmail.storage.memorystorage import MemoryStorage

        storage = MemoryStorage()
        self.test_caches(storage)