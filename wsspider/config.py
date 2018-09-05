#!/usr/bin/env python
# coding=utf-8

"""

@author: sml2h3

@license: (C) Copyright 2018-2019

@contact: sml2h3@gmail.com

@software: WsSpider

@file: config.py

@time: 2018/9/5 上午1:25
"""
from typing import Union

_config_data = {}


def _config_data_instance():
    global _config_data
    return _config_data


def set_config(key: str, value: str):
    _config_data_instance()[key] = value


def get_config(key: str, default=None) -> Union[str, None]:
    try:
        return _config_data_instance()[key]
    except KeyError:
        return default


def batch_set_config(**kwargs):
    for k, v in kwargs.items():
        set_config(k, v)