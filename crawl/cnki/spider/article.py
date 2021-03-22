import csv
import re

import requests
from bs4 import BeautifulSoup


class Article:
    title = ''
    authors = []
    summary = ''
    keys = []
    funds = []
    doi = ''
    album = ''
    special = ''
    classNo = ''

    def __init__(self,
                 url="https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CAPJ&dbname=CAPJLAST&filename"
                     "=JSJC20210309001&v=g9BjGJf5ZLUb8ZhEVCVgYMBBPhXZtERCK7a76q4xiYpmFGCyigEzyN7bUxFTs4SF"):
        print("正在获取文章主要信息")
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
        req = requests.get(url, headers=headers)
        # print(req.request.headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        # 获取文章主要信息标签
        self.doc = soup.find('div', class_="doc-top")
        print("html主要信息获取完成")

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
        print("【标题】{}爬取完成！".format(self.title))
        print("【作者】{}爬取完成！".format(self.authors))

    def crawl_summary(self):
        """爬摘要"""
        # 判断是否有摘要
        summary_tag = self.doc.find('span', id='ChDivSummary')
        if summary_tag:
            self.summary = summary_tag.text
            print("【摘要】爬取完成！")
        else:
            print("文章无摘要！")

    def crawl_keywords(self):
        """爬关键词"""
        # 判断是否有关键词
        flag = self.doc.find('p', class_='keywords')
        if flag:
            keys_tag = flag.find_all('a')
            for key_tag in keys_tag:
                k = re.sub(r'\s|;|；', '', key_tag.text)
                self.keys.append(k)
            print("【关键词】爬取完成！".format(self.keys))
        else:
            print("文章无关键词！")

    def crawl_funds(self):
        """
        爬取文章的资金资助
        """
        funds_tag = self.doc.find('p', class_='funds')
        if funds_tag:
            fs = funds_tag.find_all('a')
            for fund in fs:
                f = re.sub(r'\s|;|；', '', fund.text)
                self.funds.append(f)
            print("【资金资助】{}爬取完成！".format(self.funds))
        else:
            print("文章无资金资助！")

    def crawl_other(self):
        """获取文章其他信息的DOI，专辑，专题，分类号"""
        doi_tag = self.doc.find('span', string=re.compile("DOI"))
        album_tag = self.doc.find('span', string=re.compile("专辑"))
        special_tag = self.doc.find('span', string=re.compile("专题"))
        classNo_tag = self.doc.find('span', string=re.compile("分类号"))

        # 判断文章是否有DOI
        if doi_tag:
            self.doi = doi_tag.next_sibling.text
            print("【DOI】{}爬取完成！".format(self.doi))
        else:
            print("文章无DOI！")

        # 判断文章是否有专辑
        if album_tag:
            self.album = album_tag.next_sibling.text
            print("【专辑】{}爬取完成！".format(self.album))
        else:
            print("文章无专辑！")

        # 判断文章是否有专题
        if special_tag:
            self.special = special_tag.next_sibling.text
            print("【专题】{}爬取完成！".format(self.special))
        else:
            print("文章无专题！")

        # 判断文章是否有分类号
        if classNo_tag:
            self.classNo = classNo_tag.next_sibling.text
            print("【分类号】{}爬取完成！".format(self.classNo))
        else:
            print("文章无分类号！")

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


if __name__ == '__main__':
    a = Article(url="https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDAUTO&filename=WXJY202103002&v=1Tes7Y0J%25mmd2FPw4BHasEf4Sx6c93Huj0RsRviOBVJL08IBBs94h%25mmd2BTDQNe4KYlw4QDvz")
    f = open("../csv/article.csv", 'a+', encoding='utf-8', newline="")
    a.save_csv(f)
    f.close()
