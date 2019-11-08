# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class User(EmailBaseAPI):

    def get(self, userid):
        """
        获取成员详情
        :param userid: 员工在企业内的UserID，企业用来唯一标识用户的字段
        :return:
        """
        return self._get(
            '/cgi-bin/user/get',
            {'userid': userid}
        )