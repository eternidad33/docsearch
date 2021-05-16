import os
import unittest

from website.crawl.cnki_spiders import *

ARTICLE_URL = "dbcode=CAPJ&dbname=CAPJDAY&filename=ZZDZ20210513000"
# AUTHOR_URL = "skey=王宁&code=33167488"
# AUTHOR_URL = "skey=傅广生&code=05967496"
# AUTHOR_URL = "skey=王颖&code=07079336"
AUTHOR_URL = "skey=袁方&code=07075939"
# AUTHOR_URL = "skey=杜会静&code=07074873"
SOURCE_URL = "DBCode=cjfq&BaseID=ZZDZ"
# ORGANIZATION_URL = "sfield=in&skey=河北大学&code=0106010"
ORGANIZATION_URL = "sfield=in&skey=北京大学"
# ORGANIZATION_URL = "sfield=in&skey=武汉工程大学&code=0202782"

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "cnki"

# db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnkidemo', port=3306, charset='utf8')


db = pymysql.connect(host=MYSQL_HOST, user=USERNAME, passwd=PASSWORD, db=DATABASE, port=MYSQL_PORT, charset='utf8')


class MyTestCase(unittest.TestCase):

    def test_keyList_crawl(self):
        """测试检索页"""
        flag = False
        key = "大数据"
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
        """测试爬取单个文献"""
        article = Article(ARTICLE_URL)
        item = article.crawl()
        print(item)
        self.assertIsNotNone(item, '无')

    def test_article_store(self):
        """存储单个文献"""
        flag = False
        article = Article(ARTICLE_URL)
        try:
            article.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取文献错误")

    def test_author_crawl(self):
        """测试爬取单个作者"""
        author = Author(AUTHOR_URL)
        item = author.crawl()
        print(item)
        author.close()
        self.assertIsNotNone(item, '无')

    def test_author_store(self):
        """测试存储单个作者"""
        flag = False
        try:
            author = Author(AUTHOR_URL)
            author.store(db)
            author.close()
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取作者错误")

    def test_source_crawl(self):
        """测试爬取单个文献来源"""
        source = Source(SOURCE_URL)
        item = source.crawl()
        print(item)
        self.assertIsNotNone(item, '无')

    def test_source_store(self):
        """测试存储单个文献"""
        flag = False
        source = Source(SOURCE_URL)
        try:
            source.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取文献来源错误")

    def test_organization_crawl(self):
        """测试爬取单个组织"""
        os.chdir('..')
        organization = Organization(ORGANIZATION_URL)
        item = organization.crawl()
        print(item)
        self.assertIsNotNone(item, '无')

    def test_organization_store(self):
        """存储组织"""
        os.chdir('..')
        flag = False
        organization = Organization(ORGANIZATION_URL)
        try:
            organization.store(db)
            flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, True, "爬取组织错误")

    def test_getArticleUrls(self):
        """测试sql：未爬取的文献"""
        urls = getArticleUrls(db)
        print('需要爬取文章的个数为', len(urls))
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
        """获取未被爬取的来源列表"""
        urls = getSourceUrls(db)
        print('需要爬取的个数为', len(urls))
        for url in urls:
            print(url)
        self.assertTrue(True)

    def test_crawlSource(self):
        """爬取未被爬取的来源"""
        try:
            urls = getSourceUrls(db)
            crawlSource(urls, db)
        except:
            self.assertTrue(False, "爬取未爬取的来源异常")
        self.assertTrue(True)

    def test_getAuthor(self):
        """获取未被爬取的作者列表"""
        urls = getAuthorsUrls(db)
        print('需要爬取的个数为', len(urls))
        for url in urls:
            print(url)
        self.assertTrue(True)

    def test_crawlAuthor(self):
        """爬取未被爬取的作者"""
        try:
            urls = getAuthorsUrls(db)
            print("url的个数为", len(urls))
            print(url for url in urls)
            crawlAuthor(urls, db)
        except:
            self.assertTrue(False, "爬取未爬取的作者异常")
        self.assertTrue(True)

    def test_getOrganization(self):
        """获取未被爬取的组织列表"""
        urls = getOrganizationUrls(db)
        print('需要爬取组织的个数为', len(urls))
        for url in urls:
            print(url)
        self.assertTrue(True)

    def test_crawlOrganization(self):
        """存储未爬取的组织"""
        os.chdir('..')
        try:
            urls = getOrganizationUrls(db)
            crawlOrganization(urls, db)
        except:
            self.assertTrue(False, "爬取未爬取的组织异常")
        self.assertTrue(True)

    def test_getAuthorTS(self):
        """获取师生关系表中的未爬作者"""
        urls = getAuthorsUrls_ts(db)
        print('需要爬取作者的个数为', len(urls))
        for url in urls:
            print(url)
        self.assertTrue(True)

    def test_main(self):
        """测试主程序"""
        try:
            main(db)
        except:
            self.assertTrue(False, "主程序执行异常")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
