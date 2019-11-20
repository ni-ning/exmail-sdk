# -*- coding:utf-8 -*-
try:
    import hjson as json
except ImportError:
    import json


def _load_to_dict(d, filename=None):
    if not filename:
        filename = 'services.json-dev'

    json_obj = json.load(open(filename))
    for (k, v) in json_obj.items():
        d[k] = v


_load_to_dict(globals(), filename='services.json')
