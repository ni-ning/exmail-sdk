# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class Group(EmailBaseAPI):

    def create(self, group_data):
        '''
        创建邮件群组

        :param group_data: 创建邮件群组所需数据结构
        :return:
        '''
        return self._post(
            '/group/create',
            data=group_data
        )

    def update(self, group_data):
        '''
        更新邮件群组

        :param group_data: 更新邮件群组所需数据结构
        :return:
        '''
        return self._post(
            '/group/update',
            data=group_data
        )

    def delete(self, groupid):
        '''
        删除邮件群组

        :param groupid: 邮件群组id，邮件格式
        :return:
        '''
        return self._get(
            '/group/delete',
            {'groupid': groupid}
        )

    def get(self, groupid):
        '''
        获取邮件群组信息

        :param groupid: 邮件群组id，邮件格式
        :return:
        '''
        return self._get(
            '/group/get',
            {'groupid': groupid}
        )