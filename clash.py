import requests
import json
import time
import re
import logging
import traceback
import os
import random
import datetime
import utils
# import base64


def main(event, context):
    # 初始化日志文件
    utils.initLog('log.txt')
    utils.clearLog()
    savePoint(
        'https://subsc.ednovas.xyz/sub?target=clash&url=https://raw.githubusercontent.com/ldir92664/Vmess-Actions/main/subscribe/vmess.txt&insert=false&config=https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_MultiMode.ini&emoji=true&list=false&tfo=false&scv=false&fdn=false&sort=false&expand=true&new_name=true', 'clash.yml')


# 获取文章地址


def savePoint(url, name):
    resp = requests.get(url)
    dirs = './subscribe'
    day = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    if 'proxies' in resp.text:
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        with open(dirs + '/' + name, 'w', encoding='utf-8') as f:
            f.write(resp.text.replace('Relay_', day+'_'))
            print(name+'生成成功')


# 主函数入口
if __name__ == '__main__':
    main("", "")
