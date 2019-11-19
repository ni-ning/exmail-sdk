# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class Department(EmailBaseAPI):

    def create(self, department_data):
        '''
        创建部门

        :param department_data: 创建部门所需数据
        :return:
        '''
        return self._post(
            '/department/create',
            data=department_data
        )

    def update(self, department_data):
        '''
        创建部门

        :param department_data: 更新部门所需数据
        :return:
        '''
        return self._post(
            '/department/update',
            data=department_data
        )

    def delete(self, _id):
        '''
        删除部门

        :param _id: 部门id (注：不能删除根部门；不能删除含有子部门、成员的部门)
        :return:
        '''
        return self._get(
            '/department/delete',
            {'id': _id}
        )

    def list(self, _id=1):
        """
        获取部门列表

        :param _id: 父部门id(如果不传，默认部门为根部门，根部门ID为1)
        :return: 部门列表数据。以部门的order字段从小到大排列
        """
        return self._get(
            '/department/list',
            {'id': _id}
        )

    def search(self, name, fuzzy=False):
        '''
        查找部门

        :param name: 查找的部门名字，必须合法
        :param fuzzy: 是否模糊匹配
        :return:
        '''
        return self._post(
            '/department/search',
            data={'name': name, 'fuzzy': int(fuzzy)}
        )
