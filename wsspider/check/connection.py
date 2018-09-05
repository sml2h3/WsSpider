#!/usr/bin/env python
# coding=utf-8

"""

@author: sml2h3

@license: (C) Copyright 2018-2019

@contact: sml2h3@gmail.com

@software: WsSpider

@file: connection.py

@time: 2018/9/5 上午1:41
"""
from wsspider.config import get_config


def check_rabbitmq() -> bool:
    rabbitmq_host = get_config("host-rabbitmq", "127.0.0.1")
    rabbitmq_port = get_config("port-rabbitmq", 5672)

