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

_base_config = {
    # rabbitmq config

    "host_rabbitmq": "127.0.0.1",  # Host for rabbitmq.
    "port_rabbitmq": 5672,  # Port for Rabbitmq Server.
    "username_rabbitmq": "guest",
    "password_rabbitmq": "guest",

    # elasticsearch config
    
    "host_elastic": "127.0.0.1",  # Host for elasticsearch Server.
    "port_elastic": 9200,  # Port for ELasticsearch Server.
    "username_elastic": "elastic",
    "password_elastic": "elastic",

    # system config

    "port_msg": 39254,  # Port for this system.
    "sec_key": "6a33e893512f7a8309ae448ca1df736d",  # Make communication more believable.
    "port_web": 9999,  # Port for Website.

}


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