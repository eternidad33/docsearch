import csv
import re

import requests
from bs4 import BeautifulSoup


class Source:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}


class Journal(Source):
    """文献来源为期刊"""
    name = ''
    name_en = ''
    journals = []
    basic_info = []
    album = ''
    special = ''
    count_publish = ''

    def __init__(self, url='https://kns.cnki.net/KNS8/Navi?DBCode=cjfq&BaseID=JJWT'):
        self.url = url
        req = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        # 通过分析页面信息，要爬取的信息都存在dl标签中
        self.dl = soup.dl

    def crawl_name(self):
        """获取中英文名称"""
        # print(self.dl)
        if not self.dl:
            print('【dl标签异常】无法获取dl标签')
            return
        name_tag = self.dl.h3
        self.name = name_tag.text if name_tag else ''

        name_en_tag = name_tag.p
        self.name_en = name_en_tag.text if name_en_tag else ''
        self.name = re.sub(r'\s*|{}'.format(self.name_en), '', self.name)
        print("【中文名称】{} 爬取完成！".format(self.name))
        print("【英文名称】{} 爬取完成！".format(self.name_en))

    def crawl_journals(self):
        """获取收录机构"""
        journalType_tag = self.dl.find('p', class_="journalType")
        if not journalType_tag:
            print('【无】本期刊 {} 无收录机构'.format(self.name))
            return
        journals_tag = journalType_tag.find_all('span')
        for journal_tag in journals_tag:
            self.journals.append(journal_tag.text)
        print('【收录机构】爬取完成！')

    def crawl_basic_info(self):
        """获取基本信息"""
        ul = self.dl.find(id='JournalBaseInfo')
        if not ul:
            print('【无】无法获取 {} 的基本信息'.format(self.name))
            return
        li1 = ul.find_all('li')[1]
        ps = li1.find_all('p')
        for p in ps:
            self.basic_info.append(p.text)
            # print(p.text)
        print('【基本信息】爬取完成！')

    def crawl_publish(self):
        """获取出版信息,专辑名称,专题名称,出版文献量"""
        album_tag = self.dl.find('span', id="jiName")
        special_tag = self.dl.find('span', id="tiName")
        self.album = album_tag.text if album_tag else ''
        self.special = special_tag.text if special_tag else ''
        print('【专辑名称】{0} 爬取完成！'.format(self.album))
        print('【专题名称】{0} 爬取完成！'.format(self.special))
        try:
            publish_tag = special_tag.parent.next_sibling.next_sibling.find('span')
            self.count_publish = publish_tag.text if publish_tag else ''
            print('【出版文献量】{0} 爬取完成！\n'.format(self.count_publish))
        except:
            print('【异常】爬取出版文献量异常！url为{}\n'.format(self.url))

    def save_csv(self, file=open('../csv/source_journal.csv', 'a+', encoding='utf-8', newline="")):
        self.crawl_name()
        self.crawl_journals()
        self.crawl_basic_info()
        self.crawl_publish()
        f_csv = csv.writer(file)
        f_csv.writerow(
            (self.name, self.name_en, self.journals, self.basic_info, self.album, self.special, self.count_publish))


class School(Source):
    """文献来源为学者的论文，论文的来源为学校"""
    name = ''
    name_used = ''
    region = ''
    count_articles = ''
    count_refer = ''
    count_downloads = ''

    def __init__(self, url='https://kns.cnki.net/KNS8/Navi?DBCode=CDMD&BaseID=GHEBU'):
        self.url = url
        req = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        # 通过分析页面信息，要爬取的信息都存在dd标签中
        self.dd = soup.dd

    def crawl_name(self):
        """爬取学校名称"""
        self.name = self.dd.h3.text
        self.name = re.sub(r'\s*', '', self.name)
        print('【学校名称】{} 爬取完成！'.format(self.name))

    def crawl_base_info(self):
        """爬取基本信息,，曾用名和地域"""
        uls = self.dd.find_all('ul')
        base_tag = uls[0].find_all('li')[1]
        ps_tag = base_tag.find_all('p')
        self.name_used = ps_tag[0].span.text if ps_tag[0].span else ''
        self.region = ps_tag[1].span.text if ps_tag[1].span else ''
        print('【基本信息】爬取完成！')

    def crawl_publish_info(self):
        """爬取出版信息"""
        uls = self.dd.find_all('ul')
        if len(uls) < 2:
            return
        publish_info_tag = uls[1].find_all('li')[1]
        ps1_tag = publish_info_tag.find_all('p')
        self.count_articles = ps1_tag[0].span.text if ps1_tag[0].span else ''
        self.count_refer = ps1_tag[1].span.text if ps1_tag[1].span else ''
        self.count_downloads = ps1_tag[0].span.text if ps1_tag[0].span else ''
        print("【出版信息】爬取完成！\n")

    def save_csv(self, file=open('../csv/source_school.csv', 'a+', encoding='utf-8', newline="")):
        self.crawl_name()
        self.crawl_base_info()
        self.crawl_publish_info()
        f_csv = csv.writer(file)
        f_csv.writerow(
            (self.name, self.name_used, self.region, self.count_articles, self.count_refer, self.count_downloads))


class Newspaper(Source):
    """文献来源为报纸"""
    # TODO 爬取文献来源为报纸的信息
    pass


if __name__ == '__main__':
    base_url = 'https://kns.cnki.net'
    j1 = base_url + '/kns8/Navi?DBCode=CJFD&BaseID=HBYU'
    j2 = base_url + '/kns8/Navi?DBCode=CJFD&BaseID=DADY'
    j3 = base_url + '/kns8/Navi?DBCode=CJFD&BaseID=CRJY'
    j4 = base_url + '/KNS8/Navi?DBCode=CJFD&BaseID=ZGSM'
    j5 = base_url + '/KNS8/Navi?DBCode=CJFD&BaseID=XDSM'
    js = [j1, j2, j3, j4, j5]
    for j in js:
        journal = Journal(j)
        journal.save_csv()

    s1 = base_url + '/KNS8/Navi?DBCode=CDMD&BaseID=GBJKU'
    s2 = base_url + '/KNS8/Navi?DBCode=CDMD&BaseID=GNJDC'
    s3 = base_url + '/KNS8/Navi?DBCode=CDMD&BaseID=GHBGC'
    s4 = base_url + '/KNS8/Navi?DBCode=CDMD&BaseID=GJLIN'
    s5 = base_url + '/KNS8/Navi?DBCode=CDMD&BaseID=GKCGS'
    ss = [s1, s2, s3, s4, s5]
    for s in ss:
        s = School(s)
        s.save_csv()
