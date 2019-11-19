# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest

from exmail import SecretClient


class BaseTestCase(unittest.TestCase):

    def __init__(self):
        super(BaseTestCase, self).__init__()
        self.config = {
            'corp_id': 'xxxx',
            'corp_secret': 'yyyy'
        }
        self.client = SecretClient(self.config['corp_id'], self.config['corp_secret'])