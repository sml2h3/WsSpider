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
from .config import batch_set_config, get_config

CMD_DESCRIPTION = """{} command line mode
This command could start a thread for crawling data from http://wenshu.court.gov.cn/.
""".format(__project__)
work_path = os.getcwd()


def main(args):
    parser = argparse.ArgumentParser(description=CMD_DESCRIPTION,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--mode', '-m', type=int, default=0,
                        help="If it's 0, it's the producer, if it's 1, it's the worker, if it's 2, it's the website.")
    parser.add_argument('--host-rabbitmq', '-hr', type=str, default="127.0.0.1",
                        help="Host for rabbitmq.")
    parser.add_argument('--port-rabbitmq', '-pr', type=int, default=5672,
                        help="Port for Rabbitmq Server.")
    parser.add_argument('--host-elastic', '-he', type=str, default="127.0.0.1",
                        help="Host for elasticsearch.")
    parser.add_argument('--port-elastic', '-pe', type=int, default=9200,
                        help="Port for ELastic Server.")
    parser.add_argument('--port-msg', '-pm', type=int, default=39254,
                        help="Port for this system.")
    parser.add_argument('--sec-key', type=str, default='6a33e893512f7a8309ae448ca1df736d',
                        help='Make communication more believable.')
    parser.add_argument('--port-web', '-wp', type=int, default=9999,
                        help='Port for Website.')

    parsed_args = parser.parse_args(args)

    parsed_args_dict = vars(parsed_args)

    batch_set_config(**vars(parsed_args))

    handle_special_flags(parsed_args_dict)

    mode = get_config('mode')

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
