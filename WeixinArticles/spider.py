from urllib.parse import urlencode
import requests
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import pymongo

client = pymongo.MongoClient('localhost')
db = client['weixin']

base_url = 'https://weixin.sogou.com/weixin?'
headers = {
    'Cookie': 'GOTO=Af22578; SUID=B20361D35018910A000000005AC9EFF6; usid=NOzB6tIXkLUuALrz; SUV=0033495FD36103B25AC9EFF6DB4C4208; IPLOC=CN4401; CXID=2E38ECA6590041541C7093CA32FB0B0A; ABTEST=4|1543632326|v1; SNUID=33A45A00B7B2CC5B5F365A2BB7EC5FE1; weixinIndexVisited=1; sct=1; JSESSIONID=aaa-XKQ9rOnUreikDH6Cw; ppinf=5|1543662460|1544872060|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyOkRUfGNydDoxMDoxNTQzNjYyNDYwfHJlZm5pY2s6MjpEVHx1c2VyaWQ6NDQ6bzl0Mmx1RlNzTFk1YTFRMVhKR3lOSnBnbWdvY0B3ZWl4aW4uc29odS5jb218; pprdig=u8rKQZbHP21WSMAfvar0jl4INdUgx8yDcVedxnD0q_AzeQKcfF7E1y_dpEvi7gN9iR86r_aXrITHOyrEQ8eHSiJAq8xlLkVySqN_lqRBLp7SCqSXYgH6_6aO-LdkKAzWvT6A0IdluGjS9JsanEkKyK4EYEqomJQd-KbEFH22xxA; sgid=22-38153757-AVwCa3yjbVGjf2icq2DU8HNk; ppmdig=1543662460000000e4887ebc8b6f32fbe1696fe856e35fe2' ,
    'Host': 'weixin.sogou.com' ,
    'Referer': 'https://weixin.sogou.com/weixin?query=%E9%A3%8E%E6%99%AF&type=2&page=2' ,
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
keyword = '风景'
proxy_pool_url = 'http://127.0.0.1:5000/get'
proxy = None
max_count = 5

def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError :
        return None

def get_html(url,count=1):
    print('Crawling',url)
    print('Tring Count',count)
    global proxy
    #引入全局代理
    if count >=max_count:
        #判断请求次数
        print('Tried Too Many Counts')
        return None

    try:
        if proxy:
            proxies = {
                'http' : 'http://' + proxy
            }
            response = requests.get(url,allow_redirects=False , headers = headers,proxies = proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            #更换代理
            print('302')
            proxy = get_proxy()
            if proxy :
                print('Using Proxy',proxy)
                return get_html(url)
            else:
                print('get proxy failed')
                return None
    except ConnectionError as e :
        print('Error Occurred',e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url,count)

def get_index(keyword, page):
    data = {
        'query' : keyword,
        'type' : 2,
        'page' :page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None




def parse_detail(html):
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        data = doc('#publish_time').text()
        nickname = doc('#js_name').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        return{
            'title' : title ,
            'content' : content ,
            'data' : data ,
            'nickname' : nickname,
            'wechat' : wechat
        }

def save_to_mongo(data):
    if db['articles'].update({'title':data['title']},{'$set': data},True):
        print('Save To Mongo',data['title'])
    else:
        print('Saved to Mongo Failed',data['title'])

def main():
    for page in range(1,101):
        html = get_index(keyword,page)
        if html :
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html :
                    article_data = parse_detail(article_html)
                    print(article_data)
                    if article_data:
                        save_to_mongo(article_data)

if __name__ == '__main__':
    main()