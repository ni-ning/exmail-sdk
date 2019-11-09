腾讯企业邮开发接口
===========================================

.. module:: exmail.client

.. autoclass:: EmailClient
   :members:
   :inherited-members:

`EmailClient` 基本使用方法::

   from exmail import SecretClient

   client = SecretClient('corp_id', 'secret')  # access_token 获取方式


   user = client.user.get('userid')
   departments = client.department.list()
   # 以此类推，参见下面的 API 说明
   # client.tag.xxx()
   # client.group.xxx()

如果不提供 ``storage`` 参数，默认使用 ``exmail.storage.memorystorage.MemoryStorage`` 类型，
注意该类型不是线程安全的，而且非持久化保存，不推荐生产环境使用。

.. toctree::
   :maxdepth: 2
   :glob:

   api/*

