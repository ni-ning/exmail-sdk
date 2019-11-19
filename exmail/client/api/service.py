# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class Service(EmailBaseAPI):
    def get_login_url(self, userid):
        '''
        获取登录企业邮的url

        :param userid: 成员UserID
        :return:
        '''
        return self._get(
            '/service/get_login_url',
            {'userid': userid}
        )