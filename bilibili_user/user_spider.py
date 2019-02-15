import json
import random
import time
from urllib.parse import urlencode

import pymysql
import requests


def get_index_message(i):

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Referer': 'https://space.bilibili.com/' + str(i) + '?from=search&seid=' + str(random.randint(10000, 50000)) ,
        'Origin' : 'http://space.bilibili.com',
        'Host': 'api.bilibili.com',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    datas = {
        'mid': i,
        'jsonp': 'jsonp'
    }
    queries = urlencode(datas)
    url = 'https://api.bilibili.com/x/space/acc/info?'+queries
    result = requests.get(url,allow_redirects=False,headers=headers)
    if result.status_code == 200:
        content = json.loads(result.text)
        if content and 'data' in content.keys():
            birthday = content.get('data').get('birthday')
            coins = content.get('data').get('coins')
            face = content.get('data').get('face')
            fan_badge = content.get('data').get('fan_badge')
            jointimestamp = content.get('data').get('jointime')
            jointime_local = time.localtime(jointimestamp)
            jointime = time.strftime("%Y-%m-%d %H:%M:%S", jointime_local)
            level = content.get('data').get('level')
            mid = content.get('data').get('mid')
            moral = content.get('data').get('moral')
            name = content.get('data').get('name')
            rank = content.get('data').get('rank')
            sex = content.get('data').get('sex')
            sign = content.get('data').get('sign')
            silence = content.get('data').get('silence')
            theme = content.get('data').get('theme')
            vip_status = content.get('data').get('vip').get('status')
            vip_type = content.get('data').get('vip').get('type')
            return {
                'birthday': birthday,
                'coins': coins,
                'face':face,
                'fan_badge': fan_badge,
                'jointime': jointime,
                'level': level,
                'mid': mid,
                'moral': moral,
                'name': name,
                'rank': rank,
                'sex': sex,
                'sign': sign,
                'silence': silence,
                'theme': theme,
                'vip_status': vip_status,
                'vip_type': vip_type
            }
    else:
        print('mid为' + i + '爬取主要信息失败')


def get_follow_message(i):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Referer': 'https://space.bilibili.com/' + str(i) + '?from=search&seid=' + str(random.randint(10000, 50000)),
        'Origin': 'http://space.bilibili.com',
        'Host': 'api.bilibili.com',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    datas = {
        'mid': i,
        'jsonp': 'jsonp'
    }
    queries = urlencode(datas)
    url = 'https://api.bilibili.com/x/relation/stat?v'+queries
    html = requests.get(url, allow_redirects=False, headers=headers)
    if html.status_code == 200:
        result = json.loads(html.text)
        if result and 'data' in result.keys():
            following = result.get('data').get('following')
            black = result.get('data').get('black')
            follower = result.get('data').get('follower')
            return {
                'following': following,
                'black': black,
                'follower': follower
            }
        else:
            print('mid为' + i + '爬取关注数量等失败')


def save_to_mysql(item):
    db = pymysql.connect(host='localhost', user='root', password='123456', db='bilibili')
    cur = db.cursor()
    try:
        cur.execute('INSERT INTO bilibili_user(mid,name,sex,rank,level,fan_badge,jointime,moral,sign,'
                    'face,vip_status,vip_type,coins,silence,following,black,follower)'
                    ' VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
                    %(item['mid'], item['name'], item['sex'], item['rank'], item['level'], item['fan_badge'],
                      item['jointime'], item['moral'], item['sign'], item['face'], item['vip_status'], item['vip_type'],
                      item['coins'], item['silence'], item['following'], item['black'], item['follower']))
        db.commit()
    except Exception as e:
        print('insert failed', e)
        db.rollback()
    db.close()


def main():
    for i in range(1, 10000000):
        index_message = get_index_message(i)
        follow_message = get_follow_message(i)
        message = {}
        message.update(index_message)
        message.update(follow_message)
        print(message)
        save_to_mysql(message)
        time.sleep(2)
        

if __name__ == '__main__':
    main()