#!/bin/bash
openid=""
name=""
sfzh=""
department="信息工程学院"
Area_name="美兰校区"

curl -k -d "http://wap.hnkjedu.cn/WeChatBx/Creatfeiyanxinxi.aspx" \
    -H 'Accept: application/json, text/plain, */*' \
    -H 'Accept-Encoding: gzip, deflate' \
    -H 'Accept-Language: zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,ja-CN;q=0.6,ja;q=0.5' \
    -H 'Cache-Control: no-cache' \
    -H 'Connection: keep-alive' \
    -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8' \
    -H 'Host: wap.hnkjedu.cn' \
    -H 'Origin: http://wap.hnkjedu.cn' \
    -H 'Pragma: no-cache' \
    -H 'Referer: http://wap.hnkjedu.cn/bxxm/?openid=$openid' \
    -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1' \
    -X POST \
    -d '{\
    "openid": $openid,\
    "Area_name": $Area_name,\
    "Type": "学生",\
    "Name": $name,\
    "sfzh": $sfzh,\
    "department": $department,\
    "JCtw": "36",\
    "JWtw": "36",\
    "Zwtw": "36",\
    "Health": "健康",\
    "City": "海南省海口市美兰区",\
    "Hubei": "否",\
    "Feiyan": "否",\
    }'











