import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pyquery import PyQuery as pq
from config_1 import *
import pymongo
import time

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
#设置无头
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# browser.set_window_size(1400, 900)
wait = WebDriverWait(browser, 10)


def login(user,password):
    #模拟登陆
    browser.get('https://login.taobao.com/member/login.jhtml')
    user_login = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME,'login-switch'))
    )
    user_login.click()
    input_user = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#TPL_username_1'))
    )
    input_password = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#TPL_password_1'))
    )
    input_user.clear()
    input_user.send_keys(user)
    input_password.click()
    input_password.send_keys(password)
    login_submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_SubmitStatic'))
    )
    dragger = browser.find_element_by_id('nc_1_n1z')
    action_chains = ActionChains(browser)
    action_chains.drag_and_drop_by_offset(dragger, 300, 0).perform()

#    for index in range(500):
#        try:
#            action_chains.drag_and_drop_by_offset(dragger, 500, 0).perform()  # 平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
#        except Exception:
#            break
    time.sleep(2)

    flag = 1
    try:
        assert '验证通过' in browser.page_source
    except Exception as e :
        flag = 'move failed'

    if flag != 1:
        print(flag)
    else :
        print('move success')
        login_submit.click()
        return 1


def search(keyword):
    #搜索页
    try:
        browser.get('https://www.taobao.com')
        input_search = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )
        input_search.send_keys(keyword)
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))
        )
        get_products()
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    #请求翻页
    print('正在翻页...', page_number)
    try:
        input_page = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        input_page.clear()
        input_page.send_keys(page_number)
        submit.click()

        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number))
        )
        get_products()
    except TimeoutException:
        next_page(page_number)


def get_products():
    #分析页面 得到商品信息
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功', result)
    except Exception:
        print("存储到MONGODB错误", result)


def main():
    try:
        flag = login(user=user,password=password)
        if flag == 1:
            total = search(keyword=keyword)
            total = int(re.compile('(\d+)').search(total).group(1))
            print(total)
            for i in range(2, total + 1):
                next_page(i)
        else :
            print('登录出错')
    except Exception:
        print("浏览器关闭出错")
    finally:
        browser.close()


if __name__ == '__main__':
    main()