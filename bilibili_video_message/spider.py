import json
import time
from urllib.parse import urlencode
import threading
import pymysql
import requests

total = 0
lock = threading.Lock()

def get_request(i):
    global total
    headers = {
        'Host': 'api.bilibili.com',
        'Origin': 'https://www.bilibili.com',
        'Referer': 'https://www.bilibili.com/video/av' + str(i),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*'
    }
    datas = {'aid': i}
    queries = urlencode(datas)

    url = 'https://api.bilibili.com/x/web-interface/view?' + queries
    response = requests.get(url=url, headers=headers)
    time.sleep(0.5)
    try:
        if response.status_code == 200:
            jsdata = json.loads(response.text)
            if jsdata and 'data' in jsdata.keys():
                title = jsdata['data']['title']  # 视频名字
                tname = jsdata['data']['tname']  # 视频分区
                videos = jsdata['data']['videos']  # 视频P数
                Introduction = jsdata['data']['desc'].replace('\n', '  ')  # 视频简介
                dynamic = jsdata['data']['dynamic']  # 视频标签
                allow_submit = jsdata['data']['subtitle']['allow_submit']  # 是否允许转载
                ctimestamp = jsdata['data']['ctime']
                ctime_local = time.localtime(ctimestamp)
                ctime = time.strftime("%Y-%m-%d %H:%M:%S", ctime_local)  # 发布时间
                aid = jsdata['data']['stat']['aid']  # 视频编号
                coin = jsdata['data']['stat']['coin']  # 硬币数
                danmaku = jsdata['data']['stat']['danmaku']  # 弹幕数
                favorite = jsdata['data']['stat']['favorite']  # 收藏数
                like = jsdata['data']['stat']['like']  # 点赞数
                reply = jsdata['data']['stat']['reply']  # 评论数
                share = jsdata['data']['stat']['reply']  # 分享数
                view = jsdata['data']['stat']['view']  # 播放数
                with lock:
                    total += 1
                    return {
                        'title': title,
                        'tname': tname,
                        'videos': videos,
                        'Introduction': Introduction,
                        'dynamic': dynamic,
                        'allow_submit': allow_submit,
                        'time': ctime,
                        'aid': aid,
                        'coin': coin,
                        'danmaku': danmaku,
                        'favorite': favorite,
                        'like': like,
                        'reply': reply,
                        'share': share,
                        'view': view
                    }
    except Exception as e:
        print('爬取av号为' + str(i) + '的信息失败', e)


def save_to_mysql(item):
    db = pymysql.connect(host='localhost', user='root', password='123456', db='bilibili')
    cur = db.cursor()
    try:
        cur.execute('INSERT INTO bilibili_video_message(aid,title,tname,videos,Introduction,dynamic,allow_submit,'
                    'ctime,coin,danmaku,favorite,v_like,reply,share,view)'
                    ' VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
                    % (item['aid'], item['title'], item['tname'], item['videos'], item['Introduction'], item['dynamic'],
                       item['allow_submit'], item['time'], item['coin'], item['danmaku'], item['favorite'], item['like']
                       , item['reply'], item['share'], item['view']))
        db.commit()
    except Exception as e:
        print('插入数据失败', e)
        db.rollback()
    db.close()


def main():
    for i in range(1,3000):
        begin = i * 10000
        for j in range(begin,begin+10000):
            item = get_request(j)
            save_to_mysql(item)
            time.sleep(1)
    print('共爬取｛｝条视频信息'.format(total))


if __name__ == '__main__':
    main()
