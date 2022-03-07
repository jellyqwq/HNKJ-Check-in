# -*- coding: utf-8 -*-

import logging as log
import requests
log.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=log.INFO)

openid = '' # 签到页面抓取
Area_name = '美兰校区' # 校区
Name = '' # 姓名
sfzh = '' # 身份证号
department = '信息工程学院' # 学院
City = '海南省海口市美兰区' # 所处城市

def checkin():
    global openid, Area_name, Name, sfzh, department, City
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,ja-CN;q=0.6,ja;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'wap.hnkjedu.cn',
        'Origin': 'http://wap.hnkjedu.cn',
        'Pragma': 'no-cache',
        'Referer':'http://wap.hnkjedu.cn/bxxm/?openid={}'.format(openid),
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    }

    data = {
        'openid': openid,
        'Area_name': Area_name,
        'Type': '学生',
        'Name': Name,
        'sfzh': sfzh,
        'department': department,
        'JCtw': '36',
        'JWtw': '36',
        'Zwtw': '36',
        'Health': '健康',
        'City': City,
        'Hubei': '否',
        'Feiyan': '否',
    }

    r = requests.post(url='http://wap.hnkjedu.cn/WeChatBx/Creatfeiyanxinxi.aspx',headers=headers,data=data).json()['XXmessage']
    log.info(r)
    return r

def main(arg1,arg2):
    return checkin()