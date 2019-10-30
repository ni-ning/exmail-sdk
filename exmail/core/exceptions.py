# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import six

from exmail.core.utils import to_binary, to_text


class EmailException(Exception):

    def __init__(self, errcode, errmsg):
        """
        :param errcode: Error code
        :param errmsg: Error message
        """
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        _repr = 'Error code: {code}, message: {msg}'.format(
            code=self.errcode,
            msg=self.errmsg
        )

        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)

    def __repr__(self):
        _repr = '{klass}({code}, {msg})'.format(
            klass=self.__class__.__name__,
            code=self.errcode,
            msg=self.errmsg
        )
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)


class EmailClientException(EmailException):
    """Exmail API client exception class"""
    def __init__(self, errcode, errmsg, client=None,
                 request=None, response=None):
        super(EmailClientException, self).__init__(errcode, errmsg)
        self.client = client
        self.request = request
        self.response = response
