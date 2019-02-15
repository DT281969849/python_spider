# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Cookie': '_zap=794e2e9d-046f-448b-acf0-db3641d0cb62; __DAYU_PP=UUi3JfJUanY2zjq3vUiuffffffffef01e80c1127; d_c0="ADDn3VhABw6PTgv_SF7BcDnFQEdpXhC_AW8=|1533784798"; _xsrf=Zzva1Anjf4i8c5XxAVFuCEDYz17LRU7y; capsion_ticket="2|1:0|10:1544602091|14:capsion_ticket|44:ZGEwNjI4Y2ZhYmE5NDljMjg3YmE2OGQyM2Y0MTM1MzA=|8647b39801e0fbbd2079cc8582b3ddbfbbd324a7740905c4efb37f49c9bc7fb6"; z_c0="2|1:0|10:1544602107|4:z_c0|92:Mi4xRHZsWEJnQUFBQUFBTU9mZFdFQUhEaVlBQUFCZ0FsVk4td18tWEFESjE1S0J6TVRYMVBZRWl4M2Y1OTFnOW8tb0JR|7d156a76879fe965490a29a91c299d8fe908ea7993c267c49a086c22cb62dffa"; q_c1=82b4b172135944e5ad5ae1f751f791db|1544602127000|1522951190000; tst=r; __utma=155987696.585154877.1544687522.1544687522.1544687522.1; __utmc=155987696; __utmz=155987696.1544687522.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=1c2b7f9548c57cd7d5a535ac4812e20e',
    'Upgrade-Insecure-Requests': '1',
    'cache-control': 'max-age=0'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#   'zhihuuser.middlewares.DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihuuser.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
