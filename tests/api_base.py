# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest

from exmail import SecretClient


class BaseTestCase(unittest.TestCase):
    value = 'DM-Qm7zFYZ1-ccqOgQkMUJZYqzMk4ObP7fhlk9-X0xYxc1uP5PpZXk6I7n2I5W-dxhE2qUzRNB-U8lDoV1MwnQ'
    SecretClient.TESTING_ACCESS_TOKEN = dict(access_token=value, expires_in=5600)
    client = SecretClient()
