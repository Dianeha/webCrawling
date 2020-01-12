import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from selenium.webdriver import Chrome
import re     
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime as dt
import csv

writer = csv.writer(open('youtube.csv', 'a', encoding='utf-8', newline=''))

delay=3
driver = Chrome('/Users/multicampus/Downloads/chromedriver_win32/chromedriver')
driver.implicitly_wait(delay)

url = "https://www.youtube.com/post/UgwTy7nbBFmpq0548ap4AaABCQ"

driver.get(url)
body = driver.find_element_by_tag_name('body')

# 정렬기준 버튼 클릭
driver.find_element_by_xpath('//paper-button[@class="dropdown-trigger style-scope yt-dropdown-menu"]').click()
time.sleep(1)

# 댓글 '오래된순' 클릭
driver.find_element_by_xpath('//paper-listbox[@class="dropdown-content style-scope yt-dropdown-menu"]/a[@class="yt-simple-endpoint style-scope yt-dropdown-menu"]').click()

time.sleep(5)

# 약 4200개(100개씩 42번)의 댓글이 렌더링 될때까지 스크롤다운하고 '댓글 더보기' 클릭하는 과정
for _ in range(42):
    num_page_down = 16
    while num_page_down:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        num_page_down -= 1

    driver.find_element_by_xpath('//paper-button[@class="style-scope yt-next-continuation"]').click()
    time.sleep(5)

# 전체 소스코드 받아오기
html_source = driver.page_source
text = BeautifulSoup(html_source, 'html.parser')

# 소스코드 중 댓글 내용 부분 가져오기
comments = text.find_all('yt-formatted-string', id = "content-text")

# 댓글 개수 세면서 내용 크롤링, 4183개 되면 크롤링 멈춤
cnt = 1
for comment in comments:
    comment = comment.text.replace('\r', '').replace('\xa0', ' ').replace('\n', ' ')
    if '커뮤니티에 댓글로 남겨주세요' in comment:
        continue
    # print(cnt, "|", comment)
    # print('===============================')
    writer.writerow([cnt, comment])
    cnt += 1
    if cnt == 4183:
        break