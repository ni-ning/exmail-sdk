# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals
from tests.base import BaseTestCase


class UserTestCase(BaseTestCase):


    # def user_create(self):
    #     data = {
    #         "userid": "zhangsan001@test.oeob.cn",
    #         "name": "张三",
    #         "department": [1, ],
    #         "position": "产品经理",
    #         "mobile": "15913215XXX",
    #         "tel": "123456",
    #         "extid": "01",
    #         "gender": "1",
    #         "slaves": [],
    #         "password": "Capital123",
    #         "cpwd_login": 0
    #     }
    #     ret = self.client.user.create(data)
    #     self.assertEqual(0, ret['errcode'])
    #
    # def user_update(self):
    #     data = {
    #         "userid": "zhangsan001@test.oeob.cn",
    #         "name": "张三001",
    #     }
    #     ret = self.client.user.update(data)
    #     self.assertEqual(0, ret['errcode'])
    #
    # def user_get(self):
    #     userid = 'zhangsan001@test.oeob.cn'
    #     ret = self.client.user.get(userid)
    #     self.assertEqual(0, ret['errcode'])
    #
    # def user_batch_check(self):
    #     userid = 'zhangsan001@test.oeob.cn'
    #     ret = self.client.user.batch_check(userlist=[userid, ])
    #     self.assertEqual(0, ret['errcode'])
    #
    # def user_delete(self):
    #     userid = 'zhangsan001@test.oeob.cn'
    #     ret = self.client.user.delete(userid=userid)
    #     self.assertEqual(0, ret['errcode'])
    #
    # def user_simple_list(self):
    #     ret = self.client.user.simple_list(fetch_child=True)
    #     self.assertEqual(0, ret['errcode'])
    #     ret = self.client.user.simple_list(fetch_child=False)
    #     self.assertEqual(0, ret['errcode'])
    #
    # def user_list(self):
    #     ret = self.client.user.list(fetch_child=True)
    #     self.assertEqual(0, ret['errcode'])
    #     ret = self.client.user.list(fetch_child=False)
    #     self.assertEqual(0, ret['errcode'])

    def test_user(self):
        pass
        # self.user_create()
        # self.user_update()
        # self.user_get()
        # self.user_batch_check()
        # self.user_delete()
        # self.user_simple_list()
        # self.user_list()