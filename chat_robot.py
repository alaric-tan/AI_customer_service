'''
文件描述：基于微信公众号实现AI客服
作者：txy

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request


def get_robot_reply(question):
    '''
    函数功能：对于特定问题进行特定回复，对于非特定问题进行智能回复

    参数描述：
    question 聊天内容或问题

    返回值：str,回复内容
    '''
    if question in "你叫什么名字":
        answer = "我是用户"
    elif question in "你多少岁":
        answer = "18"
    elif question in "你是GG还是MM":
        answer = "你猜呢"
    else:
        try:
            # 调用NLP接口实现智能回复
            params = urllib.parse.urlencode(
                {'msg': question}).encode()  # 接口参数需要进行URL编码
            req = urllib.request.Request(
                "http://api.itmojun.com/chat_robot", params, method="POST")  # 创建请求对象
            # 调用接口（即向目标服务器发出http请求，并获取服务器的响应）
            answer = urllib.request.urlopen(req).read().decode()
        except Exception as e:
            answer = "AI机器人出现故障！（原因: %s）" % e

    return answer


while True:
    s = input()
    print(get_robot_reply(s))
