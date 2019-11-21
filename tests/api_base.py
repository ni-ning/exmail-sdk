# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest

import conf
from exmail import SecretClient


class BaseTestCase(unittest.TestCase):

    if conf.TESTING_ENV == 'local':
        config = getattr(conf, 'EXMAIL', {})
        client = SecretClient(config['corp_id'], config['corp_secret'])

    elif conf.TESTING_ENV == 'travis':
        import os
        print('******os.envrion******', os.environ)
        client = SecretClient(os.environ['CORP_ID'], os.environ['CORP_SECRET'])
