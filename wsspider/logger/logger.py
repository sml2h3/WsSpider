#!/usr/bin/env python
# coding=utf-8

"""

@author: sml2h3

@license: (C) Copyright 2017-2018

@contact: sml2h3@gmail.com

@software: easyprice

@file: main.py

@time: 2018/4/24 上午11:58
"""
import logging
from wsspider.cli import get_root


class Logger(object):

    def __init__(self, model):
        self.log_path = get_root() + "/logger/system.log"

        # log handler
        model = "【{}】".format(model)
        self.logger = logging.getLogger(model)
        self.logger.setLevel(logging.DEBUG)

        # file handler
        self.handler = logging.FileHandler(self.log_path)
        self.handler.setLevel(logging.WARNING)

        # command
        self.command = logging.StreamHandler()

        # format
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.command.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.addHandler(self.command)

    def info(self, msg):
        return self.logger.info(msg=msg)

    def warn(self, msg):
        return self.logger.warning(msg=msg)

    def debug(self, msg):
        return self.logger.debug(msg=msg)

    def error(self, msg):
        return self.logger.error(msg=msg)


if __name__ == '__main__':
    logger = Logger("logger.py")
    logger.error("error!")
