# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class Tag(EmailBaseAPI):

    def create(self, tag_data):
        '''
        创建标签

        :param tag_data: 创建标签所需数据结构
        :return:
        '''
        return self._post(
            '/tag/create',
            data=tag_data
        )

    def update(self, tag_data):
        '''
        更新标签

        :param tag_data: 更新标签所需数据结构
        :return:
        '''
        return self._post(
            '/tag/update',
            data=tag_data
        )

    def delete(self, tagid):
        '''
        删除标签

        :param tagid: 标签ID
        :return:
        '''
        return self._get(
            '/tag/update',
            {'tagid': tagid}
        )

    def get(self, tagid):
        '''
        获取标签成员

        :param tagid: 标签ID
        :return:
        '''
        return self._get(
            '/tag/get',
            {'tagid': tagid}
        )

    def add_tag_users(self, users_data):
        '''
        增加标签成员

        :param users_data: 增加标签成员所需数据结构
        :return:
        '''
        return self._post(
            '/tag/addtagusers',
            data=users_data
        )

    def del_tag_users(self, users_data):
        '''
        删除标签成员

        :param users_data: 删除标签成员所需数据结构
        :return:
        '''
        return self._post(
            '/tag/deltagusers',
            data=users_data
        )

    def list(self):
        '''
        获取标签列表

        '''
        return self._get(
            '/tag/list'
        )