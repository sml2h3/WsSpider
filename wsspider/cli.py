#!/usr/bin/env python
# coding=utf-8

"""

@author: sml2h3

@license: (C) Copyright 2018-2019

@contact: sml2h3@gmail.com

@software: WsSpider

@file: cli.py

@time: 2018/9/5 上午1:04
"""

import os
import sys
import argparse
from .__version__ import __version__
from .__project__ import __project__
from .config import batch_set_config, get_config, _base_config

CMD_DESCRIPTION = """{} command line mode
This command could start a thread for crawling data from http://wenshu.court.gov.cn/.
""".format(__project__)
work_path = os.getcwd()


def main(args):
    parser = argparse.ArgumentParser(description=CMD_DESCRIPTION,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--mode', '-m', type=int, default=0,
                        help="If it's 0, it's the producer, if it's 1, it's the worker, if it's 2, it's the website.")
    parser.add_argument('--test', action='store_true', default=False,
                        help="start debug mode")
    parser.add_argument('--test_model', '-tm', type=str, default='installtion',
                        help="The model which you want to test.")
    parser.add_argument('--debug', '-d', action="store_true", default=False,
                        help="debug mode")

    parsed_args = parser.parse_args(args)

    parsed_args_dict = vars(parsed_args)

    batch_set_config(**vars(parsed_args))

    batch_set_config(**_base_config)

    handle_special_flags(parsed_args_dict)

    mode = get_config('mode')

    test = get_config('test')

    if test:
        test_model = get_config('test_model')
        if test_model == 'installtion':
            from .test.installtion import debug
            debug()
        if test_model == 'rabbitmq':
            from .test.rabbitmq import debug
            debug()
        if test_model == 'elastic':
            from .test.elastic import debug
            debug()

    if mode == 0:
        from .producer.app import app_start
        app_start()
    elif mode == 1:
        pass
    elif mode == 2:
        pass
    else:
        return 0


def get_root():
    # get project base dir
    return os.path.dirname(os.path.abspath(__file__))


def app_start():
    sys.exit(main(sys.argv[1:]))


def handle_special_flags(args: dict):
    if "version" in args and args['version']:
        print('v{}'.format(__version__))
        sys.exit(0)
