#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
import threading
import time
import os
import re
import requests

header={
    'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0;',
    'Cookie':'rememberMe=xxx'

    }
check="rememberMe"

lock = threading.Lock()
http_URL = []

#网站url
http_website  = []
#每个线程分配的url
urlSepList=[]
#分离文件名 给每个线程分一个
def read_file(file_path):
    # 判断文件路径是否存在，如果不存在直接退出，否则读取文件内容
    if not os.path.exists(file_path):
        print('Please confirm correct filepath !')
        sys.exit(0)
    else:
        with open(file_path, 'r') as source:
            for line in source:
                #print(line.rstrip('\r\n').rstrip('\n'))
                http_website.append(line.rstrip('\r\n').rstrip('\n'))

#分离文件名 给每个线程分一个
def separateName(threadCount):
    for i in range(0,len(http_website),int(len(http_website)/threadCount)):
        urlSepList.append(http_website[i:i+int(len(http_website)/threadCount)])

#多线程函数
def multithreading(threadCount):
    separateName(threadCount)#先分离
    for i in range(0,threadCount-1):
        t=threading.Thread(target=run_one_thread,args=(urlSepList[i],))
        t.start()

#每个线程的运作 参数为文件名称的列表
def run_one_thread(url_list):
    port=8009
    for line in url_list:
        try:
            line=line.replace('\n','').replace('\r','')
            k = requests.get(line,headers=header,verify=False,timeout=2)
            l = str(k.headers)
            if check in l:
                f=open("shiro.txt","a+")
                print("[+ "+"存在shiro:"+line)
                f.write(line+"\n")
                f.close()
            else:
               
                print("[- "+"无shiro:"+line)
        except Exception as e:
            pass
if __name__ == '__main__':
    file_str="ip.txt"
    read_file(file_str)
    thread_num=100
    if len(http_website)<thread_num:
        thread_num=len(http_website)
    print(thread_num)
    multithreading(thread_num)
   # print(urlSepList)