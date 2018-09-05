#!/usr/bin/env python
# coding=utf-8

"""

@author: sml2h3

@license: (C) Copyright 2018-2019

@contact: sml2h3@gmail.com

@software: easyprice

@file: __init__.py.py

@time: 2018/9/5 上午12:51
"""


from .logger.logger import Logger
from .__version__ import __version__
from .__author__ import __author__
from .__author__ import __copyright__
from .__project__ import __project__
logger = Logger("INIT")

logger.info("Wait me ...")
logger.info("Welcome to {} System".format(__project__))
logger.info("Now Version is : {}".format(__version__))
logger.info("【Copyright】: {}".format(__copyright__))
logger.info("【Author】: {}".format(__author__))
