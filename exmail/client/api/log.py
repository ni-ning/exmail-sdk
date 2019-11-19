# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from exmail.client.api.base import EmailBaseAPI


class Log(EmailBaseAPI):

    def mail_status(self, data):
        '''
        查询邮件概况

        :param data: 请求包结构体
        :return:
        '''
        return self._post(
            '/log/mailstatus',
            data=data
        )

    def mail(self, data):
        '''
        查询邮件

        :param data: 请求包结构体
        :return:
        '''
        return self._post(
            '/log/mail',
            data=data
        )

    def login(self, data):
        '''
        查询成员登录

        :param data: 请求包结构体
        :return:
        '''
        return self._post(
            '/log/login',
            data=data
        )

    def batch_job(self, data):
        '''
        查询批量任务

        :param data: 请求包结构体
        :return:
        '''
        return self._post(
            '/log/batchjob',
            data=data
        )

    def operation(self, data):
        '''
        查询操作记录

        :param data: 请求包结构体
        :return:
        '''
        return self._post(
            '/log/operation',
            data=data
        )


