# -*- coding:utf-8 -*-
import os
try:
    import hjson as json
except ImportError:
    import json


def _load_to_dict(d, filename=None):
    if not filename:
        filename = 'dev-services.json'

    json_obj = json.load(open(filename))
    for (k, v) in json_obj.items():
        d[k] = v


# 测试环境 local 本地测试，需要提供 services.json文件
# 测试环境 travis 根据travis提供环境变量
TESTING_ENV = 'travis'   # ['local', 'travis']

if TESTING_ENV == 'local':
    _load_to_dict(globals(), filename='services.json')
