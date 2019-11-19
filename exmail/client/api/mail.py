# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class Mail(EmailBaseAPI):

    def new_count(self, data):
        '''
        查询邮件

        :param data: 请求包结构体
        :return:
        '''
        return self._post(
            '/mail/newcount',
            data=data
        )