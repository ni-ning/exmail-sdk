# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest

import conf
from exmail import SecretClient


class BaseTestCase(unittest.TestCase):
    config = getattr(conf, 'EXMAIL', {})
    client = SecretClient(config['corp_id'], config['corp_secret'])