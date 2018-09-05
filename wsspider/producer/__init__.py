#!/usr/bin/env python
# coding=utf-8

"""

@author: sml2h3

@license: (C) Copyright 2018-2019

@contact: sml2h3@gmail.com

@software: WsSpider

@file: __init__.py.py

@time: 2018/9/5 上午1:35
"""
import sys
from wsspider.config import get_config
from wsspider.logger.logger import Logger
from wsspider.check.connection import check_rabbitmq, check_elastic

logger = Logger("producer")

logger.info("Initializing...")

# check mode is debug?
debug = get_config("debug")

if not debug:
    # check RabbitMq is started
    logger.info("Checking configure...")
    rabbitmq_status = check_rabbitmq()
    if not rabbitmq_status:
        sys.exit(0)

    # check Elastic
    elastic_status = check_elastic()
    if not elastic_status:
        sys.exit(0)

logger.info("Welcome to use WsSpider's Producer System!")
