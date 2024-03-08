"""
Created on 2024-03-07
@author:yc
@description: 空间站数据搜索服务
"""
import json
import requests


def get_kjz_data(_url, _query, *args, **kwargs):
    """
    :param _url:
    :param _query:
    :return:
    """
    res = requests.post(_url, data=json.dumps(_query), verify=False, *args, **kwargs)
    return res.json()
