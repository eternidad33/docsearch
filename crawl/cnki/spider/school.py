import csv
import re

import requests
from bs4 import BeautifulSoup


class School:
    name = ''
    name_used = ''
    region = ''
    official_website = ''

    def __init__(self,
                 url='https://kns.cnki.net/kcms/detail/knetsearch.aspx?sfield=in&skey=%E6%B2%B3%E5%8C%97%E5%A4%A7%E5'
                     '%AD%A6&code=0106010'):
        self.url = url
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
        req = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(req.text, 'html.parser')

    def crawl(self):
        # 获取名称
        self.name = self.soup.h1.text if self.soup.h1 else ''

        # 获取主要信息的div
        rowall = self.soup.find('div', class_='rowall')

        # 获取曾用名，地域，网址
        name_used_span = rowall.find('span', string=re.compile('曾用名'))
        region_span = rowall.find('span', string=re.compile('地域'))
        official_website_span = rowall.find('span', string=re.compile('网址'))
        self.name_used = name_used_span.next_sibling.text if name_used_span.next_sibling else ''
        self.region = region_span.next_sibling.text if region_span.next_sibling else ''
        self.official_website = official_website_span.next_sibling.text if official_website_span.next_sibling else ''

    def save_csv(self, f):
        self.crawl()
        f_csv = csv.writer(f)
        f_csv.writerow((self.name, self.name_used, self.region, self.official_website))


if __name__ == '__main__':
    f = open('../csv/school.csv', 'a+', encoding='utf-8', newline="")
    a = School()
    a.save_csv(f)
