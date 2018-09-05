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
import pika
import requests
from requests.auth import HTTPBasicAuth
from wsspider.config import get_config
from wsspider.logger.logger import Logger

logger = Logger("check->connection")


def check_rabbitmq() -> bool:
    logger.info("checking rabbitmq")
    rabbitmq_host = get_config("host_rabbitmq", "127.0.0.1")
    rabbitmq_port = get_config("port_rabbitmq", 5672)
    rabbitmq_username = get_config("username_rabbitmq", 'guest')
    rabbitmq_password = get_config("password_rabbitmq", 'guest')

    credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host, int(rabbitmq_port), '/', credentials))
    except pika.exceptions.ConnectionClosed as e:
        logger.warn("RabbitMq Server Connect failed! Please check RabbitMq host and port is correct!")
        return False
    except pika.exceptions.ProbableAuthenticationError as e:
        logger.warn("RabbitMq Server Auth failed! Please check RabbitMq username and password is correct!")
        return False
    logger.info("RabbitMq Server Started!")
    return True


def check_elastic() -> bool:
    logger.info("checking elasticsearch")
    elastic_host = get_config("host_elastic")
    elastic_port = get_config("port_elastic")
    elastic_username = get_config("username_elastic")
    elastic_password = get_config("password_elastic")
    elastic_link = "http://{}:{}/".format(elastic_host, elastic_port)
    logger.info("We will try connect to {}".format(elastic_link))
    try:
        rsp = requests.get(elastic_link, auth=HTTPBasicAuth(username=elastic_username, password=elastic_password))
    except requests.exceptions.ConnectionError as e:
        logger.warn("Elasticsearch Server Connect failed! Please check Elasticsearch host and port is correct!")
        return False
    if 'security_exception' in rsp.text:
        logger.warn("Elasticsearch Server Auth failed! Please check Elasticsearch username and password is correct!")
        return False
    logger.info("Elasticsearch Server Started!")
    return True
