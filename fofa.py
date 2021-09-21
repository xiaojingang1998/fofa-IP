#!/usr/bin/env python
# encoding: utf-8

import requests
import re
import base64


def init():
    fofa_token = ""  # 此处填入 fofo_token
    user = ""  # 此处填入 user
    query = ''  # 此处填入查询语句
    return fofa_token, user, query


def getIp(YY=init()):
    IP=[]
    headers = {"Cookie" : "befor_router=%%2f; fofa_token=%s; user=%s"%(YY[0],YY[1])}

    # 获取IP string
    for i in range(1,6):
        response = requests.get("https://fofa.so/result?qbase64=%s&page=%s&page_size=10"%(str(base64.b64encode(YY[2].encode('utf-8')),'utf-8'),i), headers = headers)
        IP += re.findall(r"<a href=\".*\" target=\"_blank\">", response.text)
    # 处理IP string 为 IP,并将结果写入 IP.txt
    with open("IP.txt", "w") as ip:
        for i in IP:
            ip.write(i.split("\"")[1]+"\n")


if __name__ == '__main__':
    getIp()
