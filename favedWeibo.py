#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoliang'
__email__ = 'zhaoliang@iflytek.com'
__create__ = '2014/11/29'

from weibo import Client
import codecs

# 前往新浪微博开放平台申请应用，补充上下面的参数
API_KEY = 'xxxx'
API_SECRET = 'xxxx'
REDIRECT_URI = 'xxxx'
USER_NAME = 'xxxx'
USER_PASSWORD = 'xxxx'

c = Client(API_KEY, API_SECRET, REDIRECT_URI, username=USER_NAME, password=USER_PASSWORD)


def md_escape(md):
    escape_char = ['\\', '`', '*', '_', '{', '}', '(', ')', '[', ']', '#', '+', '-', '!', '~']
    for char in escape_char:
        md = md.replace(char, '\\'+char)
    return md


def status2md(weibo_status):
    if weibo_status.get('user', None):
        user_name = weibo_status['user']['name']
        user_profile_url = 'http://weibo.com/' + weibo_status['user']['profile_url']
        weibo_content = md_escape(weibo_status['text'])
        weibo_pic = weibo_status.get('original_pic', None)
        weibo_pic_mid_thumb = weibo_status.get('bmiddle_pic', None)
        weibo_pic_addition = ''
        if weibo_pic:
            weibo_pic_addition = u'([点击查看原始配图](%s))\n<img src="%s" style="max-height:300px;"/>' % (weibo_pic, weibo_pic_mid_thumb)
        return '[**%s**](%s)\n%s\n%s' % (
            user_name, user_profile_url, weibo_content, weibo_pic_addition
        )
    return ''

md_file = codecs.open('1.md', 'w+', 'utf-8')
for i in range(1, 100):
    faved_weibos = c.get('favorites', count=20, page=i)
    if not faved_weibos['favorites']:
        break
    for weibo in faved_weibos['favorites']:
        md_string = ''
        md_string += '- ' + status2md(weibo['status'])
        if weibo['status'].get('retweeted_status', None):
            md_string += '\n> ' + status2md(weibo['status']['retweeted_status']) + '\n'
        md_string += '\n---\n'
        md_file.write(md_string)
if md_file:
    md_file.close()