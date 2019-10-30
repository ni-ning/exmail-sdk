# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class Department(EmailBaseAPI):
    def list(self, _id=1):
        """
        获取部门列表
        :param _id: 父部门id(如果不传，默认部门为根部门，根部门ID为1)
        :return: 部门列表数据。以部门的order字段从小到大排列
        """
        return self._get(
            '/department/list',
            {'id': _id},
            result_processor=lambda x: x['department']
        )