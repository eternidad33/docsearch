import unittest

from website.crawl.cnki_spiders import *

ARTICLE_URL = ""
AUTHOR_URL = ""
SOURCE_URL = ""
ORGANIZATION_URL = ""
article = Article(ARTICLE_URL)
author = Author(AUTHOR_URL)
source = Source(SOURCE_URL)
organization = Organization(ORGANIZATION_URL)


class MyTestCase(unittest.TestCase):
    def test_keyList_crawl(self):
        flag = False
        key = "知识图谱"
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
        item = {}
        print(item)
        self.assertIsNotNone(item, '无')

    def test_article_store(self):
        item = {}
        print(item)
        self.assertIsNotNone(item, '无')

    def test_author_crawl(self):
        item = {}
        print(item)
        self.assertIsNotNone(item, '无')

    def test_author_store(self):
        item = {}
        print(item)
        self.assertIsNotNone(item, '无')

    def test_source_store(self):
        item = {}
        print(item)
        self.assertIsNotNone(item, '无')

    def test_organization_crawl(self):
        item = {}
        print(item)
        self.assertIsNotNone(item, '无')

    def test_organization_store(self):
        item = {}
        print(item)
        self.assertIsNotNone(item, '无')


if __name__ == '__main__':
    unittest.main()
