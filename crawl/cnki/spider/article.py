import csv
import re

import pymysql
import requests
from bs4 import BeautifulSoup


class Article:
    title = 'None'
    authors = []
    summary = 'None'
    keys = ''
    funds = ''
    doi = 'None'
    album = 'None'
    special = 'None'
    classNo = 'None'

    def __init__(self, url="FileName=XAJD20210319000&DbName=CAPJLAST&DbCode=CAPJ&"):
        # print("正在获取文章主要信息")
        self.url = url
        new_url = "https://kns.cnki.net/kcms/detail/detail.aspx?" + self.url
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
        req = requests.get(new_url, headers=headers)
        # print(req.request.headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        # 获取文章主要信息标签
        self.doc = soup.find('div', class_="doc-top")
        # print("html主要信息获取完成")
        self.db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnki', port=3306, charset='utf8')
        self.curr = self.db.cursor()

    def crawl_main(self):
        """
        爬取文章标题，作者
        """
        # 获取文章标题
        self.title = self.doc.h1.text

        # 作者列表
        author_list_tag = self.doc.find('h3', id="authorpart")
        # 获取作者名称
        for author_tag in author_list_tag:
            name = re.sub(r'\d+,\d+', '', author_tag.text)
            self.authors.append(name)
        # print("【标题】{}爬取完成！".format(self.title))
        # print("【作者】{}爬取完成！".format(self.authors))

    def crawl_summary(self):
        """爬摘要"""
        # 判断是否有摘要
        summary_tag = self.doc.find('span', id='ChDivSummary')
        if summary_tag:
            self.summary = summary_tag.text
            # print("【摘要】爬取完成！")
        else:
            print("【无】{} 无摘要！".format(self.title))

    def crawl_keywords(self):
        """爬关键词"""
        # 判断是否有关键词
        flag = self.doc.find('p', class_='keywords')
        key_list = []
        if flag:
            keys_tag = flag.find_all('a')
            for key_tag in keys_tag:
                k = re.sub(r'\s|;|；', '', key_tag.text)
                key_list.append(k)
            self.keys = str(key_list)
            # print("【关键词】爬取完成！".format(self.keys))
        else:
            print("【无】{} 无关键词！".format(self.title))

    def crawl_funds(self):
        """
        爬取文章的资金资助
        """
        funds_tag = self.doc.find('p', class_='funds')
        funds_list = []
        if funds_tag:
            fs = funds_tag.find_all('a')
            for fund in fs:
                f = re.sub(r'\s|;|；', '', fund.text)
                funds_list.append(f)
            self.funds = str(funds_list)
            # print("【资金资助】{}爬取完成！".format(self.funds))
        else:
            print("【无】{} 无资金资助！".format(self.title))

    def crawl_other(self):
        """获取文章其他信息的DOI，专辑，专题，分类号"""
        doi_tag = self.doc.find('span', string=re.compile("DOI"))
        album_tag = self.doc.find('span', string=re.compile("专辑"))
        special_tag = self.doc.find('span', string=re.compile("专题"))
        classNo_tag = self.doc.find('span', string=re.compile("分类号"))

        # 判断文章是否有DOI
        if doi_tag:
            self.doi = doi_tag.next_sibling.text
            # print("【DOI】{}爬取完成！".format(self.doi))
        else:
            print("【无】{} 无DOI！".format(self.title))

        # 判断文章是否有专辑
        if album_tag:
            self.album = album_tag.next_sibling.text
            # print("【专辑】{}爬取完成！".format(self.album))
        else:
            print("【无】{} 无专辑！".format(self.title))

        # 判断文章是否有专题
        if special_tag:
            self.special = special_tag.next_sibling.text
            # print("【专题】{}爬取完成！".format(self.special))
        else:
            print("【无】{} 文章无专题！".format(self.title))

        # 判断文章是否有分类号
        if classNo_tag:
            self.classNo = classNo_tag.next_sibling.text
            # print("【分类号】{}爬取完成！".format(self.classNo))
        else:
            print("【无】{} 无分类号！".format(self.title))

    def save_csv(self, f):
        self.crawl_main()
        self.crawl_summary()
        self.crawl_keywords()
        self.crawl_funds()
        self.crawl_other()
        f_csv = csv.writer(f)
        f_csv.writerow((self.title, self.authors, self.summary, self.keys, self.funds, self.doi, self.album,
                        self.special, self.classNo))
        print("【文章】{}已存储到CSV文件中！".format(self.title))

    def spider(self):
        """返回爬取到的文章信息,边爬边存
        :return: 标题,摘要,关键词,资助机构,doi,专辑,专题,分类号
        """
        self.crawl_main()
        self.crawl_summary()
        self.crawl_keywords()
        self.crawl_funds()
        self.crawl_other()
        keys = re.sub(r"'", '"', self.keys)
        funds = re.sub(r"'", '"', self.funds)
        return self.title, self.summary, keys, funds, self.doi, self.album, self.special, self.classNo
        # title, summary, keys, funds, doi, album, special, classNo = self.title, self.summary, self.keys,
        # self.funds, self.doi, self.album, self.special, self.classNo keys = re.sub(r"'", '"', str(keys)) funds =
        # re.sub(r"'", '"', str(funds)) sql_insert_article = "insert into article(url,title, summary, keyss, funds,
        # doi, album, special, classNo) " \ "values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(self.url,
        # title, summary, keys, funds, doi, album, special, classNo) try: self.curr.execute(sql_insert_article)
        # self.db.commit() print('【成功】{}'.title()) except: print('插入文章异常') self.db.rollback()


if __name__ == '__main__':
    a = Article(
        url="dbcode=CJFD&dbname=CJFDAUTO&filename=WXJY202103002&v=1Tes7Y0J%25mmd2FPw4BHasEf4Sx6c93Huj0RsRviOBVJL08IBBs94h%25mmd2BTDQNe4KYlw4QDvz")
    f = open("../csv/article.csv", 'a+', encoding='utf-8', newline="")
    a.save_csv(f)
    f.close()
