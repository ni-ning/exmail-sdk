# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class User(EmailBaseAPI):

    def create(self, user_data):
        '''
        创建成员

        :param user_data: 用户信息
        :return:
        '''
        return self._post(
            '/user/create',
            data=user_data
        )

    def update(self, user_data):
        '''
        更新成员

        :param user_data: 用户信息
        :return:
        '''
        return self._post(
            '/user/update',
            data=user_data
        )

    def delete(self, userid):
        '''
        删除成员

        :param userid: 员工在企业邮的邮箱，企业用来唯一标识用户的字段
        :return:
        '''
        return self._get(
            '/user/delete',
            {'userid': userid}
        )

    def get(self, userid):
        """
        获取成员详情

        :param userid: 员工在企业邮的邮箱，企业用来唯一标识用户的字段
        :return:
        """
        return self._get(
            '/user/get',
            {'userid': userid}
        )

    def simple_list(self, department_id=1, fetch_child=False):
        '''
        获取部门成员

        :param department_id: 获取的部门id。id为1时可获取根部门下的成员
        :param fetch_child:  是否递归获取子部门下面的成员
        :return:
        '''
        return self._get(
            '/user/simplelist',
            {'department_id': department_id, 'fetch_child': int(fetch_child)}
        )

    def list(self, department_id=1, fetch_child=False):
        '''
        获取部门成员(详情)

        :param department_id: 获取的部门id。id为1时可获取根部门下的成员
        :param fetch_child: 是否递归获取子部门下面的成员
        :return:
        '''
        return self._get(
            '/user/list',
            {'department_id': department_id, 'fetch_child': int(fetch_child)}
        )

    def batch_check(self, userlist):
        '''
        批量检查账号

        :param userlist: 邮件账号列表
        :return:
        '''
        return self._post(
            '/user/batchcheck',
            data={'userlist': userlist}
        )
