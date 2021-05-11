import re
import time

import pymysql
import redis
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class KeyList:
    """关键词列表
    爬取关系，文献发表日期
    关系：文献-来源，文献-作者，存入MySQL关系表中
    发布日期：爬取后存入redis或者直接爬取
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.cnki.net/")
        print("全局等待时间设置为3秒")
        self.driver.implicitly_wait(3)
        print("窗口最大化")
        self.driver.maximize_window()
        self.db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnki', port=3306, charset='utf8')
        self.curr = self.db.cursor()
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def _input_keyword(self, keyword):
        """输入关键词"""
        print("输入的关键词为：{}".format(keyword))
        key_input = self.driver.find_element_by_id("txt_SearchText")
        key_input.send_keys(keyword)
        key_input.send_keys(Keys.RETURN)

    def _crawl_qikan(self):
        """爬取期刊"""
        # 选择期刊
        try:
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/ul[1]/li[1]/a").click()
        except Exception as e:
            print(e)
            return
        for i in range(3):
            # todo 爬取期刊行数据并存入mysql对应关系表
            next_tag = self.driver.find_element_by_xpath('//*[@id="PageNext"]')
            next_tag.click()
            time.sleep(2)

    def _crawl_lunwen(self):
        """爬取论文"""
        try:
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/ul[1]/li[2]/a").click()
        except Exception as e:
            print(e)
            return
        for i in range(3):
            # todo 爬取论文行数据并存入mysql相应关系表
            next_tag = self.driver.find_element_by_xpath('//*[@id="PageNext"]')
            next_tag.click()
            time.sleep(2)

    def crawl(self, keyword):
        """爬取本列表的期刊和论文"""
        self._input_keyword(keyword)
        self._crawl_qikan()
        self._crawl_lunwen()
        # 关闭资源
        self.driver.close()
        self.db.close()
        self.r.close()


class Article:
    """文章详情页
    发布日期以键值对形式存到Redis
    直接获取到的信息：标题，摘要，关键词
    作者链接
    """

    def __init__(self, url="FileName=XAJD20210319000&DbName=CAPJLAST&DbCode=CAPJ&"):
        self.url = "https://kns.cnki.net/kcms/detail/detail.aspx?" + url
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parse')
        # 获取文章主要信息标签
        self.doc = soup.find('div', class_="doc-top")
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def crawl(self):
        """爬取文章详情页
        返回字典类型数据，标题title，摘要summary，关键词keys，作者authors，发布日期date
        """

        # 获取文章标题
        item = {'title': self.doc.h1.text}

        author_list_tag = self.doc.find('h3', id="authorpart")  # 作者列表
        authors = []
        for author_tag in author_list_tag:
            # todo 解析作者链接
            url = ""
            authors.append(url)
            # name = re.sub(r'\d+,\d+', '', author_tag.text)
        item['authors'] = authors

        summary_tag = self.doc.find('span', id='ChDivSummary')
        item['summary'] = summary_tag.text if summary_tag else ''

        # 判断是否有关键词
        flag = self.doc.find('p', class_='keywords')
        key_list = []
        if flag:
            keys_tag = flag.find_all('a')
            for key_tag in keys_tag:
                k = re.sub(r'\s|;|；', '', key_tag.text)
                key_list.append(k)
            item['keys'] = str(key_list)
        else:
            item['keys'] = ''

        # todo 从redis中获取发布日期

        self.r.close()
        return item

    def store(self):
        """存储数据
        article表和re_article_author表
        """
        item = self.crawl()


class Author:
    """作者详情页
    信息：主修专业，总发文量，总下载量
    关系：作者-文献，师生，所在机构
    """

    def __init__(self):
        pass

    def crawl(self):
        """爬取"""
        pass

    def store(self, curr):
        pass


class Source:
    """文献来源
    信息：名称，基本信息，出版信息，评估信息
    关系：文献链接
    """

    def __init__(self):
        pass


class Organization:
    """作者机构

    """

    def __init__(self):
        pass


def getArticleUrls():
    """获取未被爬取的文献链接"""
    pass


def getAuthorsUrls():
    """获取未被爬取的作者链接"""
    pass


def getSourceUrls():
    """获取未被爬取的文献来源链接"""
    pass


def getOrganizationUrls():
    """获取未被爬取的文献来源链接"""
    pass


def crawlArticle(urls):
    """爬取未被爬取的文章"""
    pass


def crawlAuthor(urls):
    """爬取未被爬取的作者"""
    pass


def crawlSource(urls):
    """爬取未被爬取的文献来源"""
    pass


def crawlOrganization(urls):
    """爬取未被爬取的学者所在单位"""
    pass


if __name__ == '__main__':
    k = KeyList()
    # 输入关键词查询
    k.crawl("知识图谱")
