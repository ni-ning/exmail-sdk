# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class Option(EmailBaseAPI):
    def get(self, data):
        '''
        获取功能属性

        :param data: 请求包结构体
        :return:
        '''
        return self._post(
            '/useroption/get',
            data=data
        )

    def update(self, data):
        '''
        更改功能属性

        :param data: 请求包结构体
        :return:
        '''
        return self._post(
            '/useroption/update',
            data=data
        )