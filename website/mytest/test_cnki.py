import unittest

from website.crawl.cnki_spiders import *

ARTICLE_URL = "dbcode=CAPJ&dbname=CAPJDAY&filename=ZZDZ20210513000"
AUTHOR_URL = "skey=王宁&code=33167488"
SOURCE_URL = "DBCode=cjfq&BaseID=ZZDZ"
ORGANIZATION_URL = "DBCode=CDMD&BaseID=GBYDU"
article = Article(ARTICLE_URL)
author = Author(AUTHOR_URL)
source = Source(SOURCE_URL)
organization = Organization(ORGANIZATION_URL)
db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnkidemo', port=3306, charset='utf8')


class MyTestCase(unittest.TestCase):
    def test_keyList_crawl(self):
        flag = False
        key = "人工智能"
        try:
            k = KeyList()
            k.input_keyword(key)
            k.crawl_qikan()
            k.crawl_lunwen()
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取关键词列表错误")

    def test_article_crawl(self):
        item = article.crawl()
        print(item)
        self.assertIsNotNone(item, '无')

    def test_article_store(self):
        flag = False
        try:
            article.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取文献错误")

    def test_author_crawl(self):
        item = author.crawl()
        print(item)
        self.assertIsNotNone(item, '无')

    def test_author_store(self):
        flag = False
        try:
            author.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取作者错误")

    def test_source_crawl(self):
        item = source.crawl()
        print(item)
        self.assertIsNotNone(item, '无')

    def test_source_store(self):
        flag = False
        try:
            source.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取文献来源错误")

    def test_organization_crawl(self):
        item = {}
        print(item)
        self.assertIsNotNone(item, '无')

    def test_organization_store(self):
        flag = False
        try:
            organization.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取组织错误")

    def test_getArticleUrls(self):
        """测试sql：未爬取的文献"""
        urls = getArticleUrls(db)
        print('需要爬取的个数为', len(urls))
        for url in urls:
            print(url)
        self.assertTrue(True)

    def test_crawlArticle(self):
        """测试：爬取并存储未爬取的文章"""
        try:
            urls = getArticleUrls(db)
            crawlArticle(urls, db)
        except:
            self.assertTrue(False, "爬取未爬取的文章异常")
        self.assertTrue(True)

    def test_getSource(self):
        urls = getSourceUrls(db)
        print('需要爬取的个数为', len(urls))
        for url in urls:
            print(url)
        self.assertTrue(True)

    def test_crawlSource(self):
        try:
            urls = getSourceUrls(db)
            crawlSource(urls, db)
        except:
            self.assertTrue(False, "爬取未爬取的文章异常")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
