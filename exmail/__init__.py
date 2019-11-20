# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from exmail.client import SecretClient
from exmail.core.exceptions import EmailClientException, EmailException


__VERSION__ = '1.0.0'
__AUTHOR__ = 'ni-ning'


# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
