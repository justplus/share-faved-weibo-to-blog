#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoliang'
__email__ = 'zhaoliang@iflytek.com'
__create__ = '2014/11/29'

from setuptools import setup

setup(
    name='favedWeibo',
    version='0.1',
    description='python script to export faved sina weibos to markdown file',
    author='zhaoliang',
    author_email='zhaoliang@iflytek.com',
    install_requires=[
        "weibo"
    ]
)