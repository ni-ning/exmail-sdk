# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from tests.api_base import BaseTestCase


class DepartmentTestCase(BaseTestCase):
    dept_id = 4913577855806636138

    def department_create(self):
        data = {
            "name": "测试部门000001",
            "parentid": self.dept_id
        }
        ret = self.client.department.create(data)
        self.assertEqual(0, ret['errcode'])
        return ret['id']

    def department_update(self, _id):
        data = {
            "name": "测试部门0000002",
            "id": _id,
        }
        ret = self.client.department.update(data)
        self.assertEqual(0, ret['errcode'])

    def department_delete(self, _id):
        ret = self.client.department.delete(_id)
        self.assertEqual(0, ret['errcode'])

    def department_list(self, _id):
        ret = self.client.department.list(_id)
        self.assertEqual(0, ret['errcode'])

    def department_search(self):
        ret = self.client.department.search('信息技术')
        self.assertEqual(0, ret['errcode'])

    def test_department(self):
        dept_id = self.department_create()
        self.department_update(dept_id)
        self.department_list(dept_id)
        self.department_delete(dept_id)
        self.department_search()
