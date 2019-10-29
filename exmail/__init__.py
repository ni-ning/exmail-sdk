# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

__VERSION__ = '0.0.1'
__AUTHOR__ = 'ni-ning'


# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())