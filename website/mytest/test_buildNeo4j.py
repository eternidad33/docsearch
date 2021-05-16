import unittest

import pymysql
from py2neo import Graph

from website.crawl.build_neo4j import *

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "cnkidemo"

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379


class MyTestCase(unittest.TestCase):
    def test_setStatus(self):
        try:
            db = pymysql.connect(host=MYSQL_HOST, user=USERNAME, passwd=PASSWORD, db=DATABASE, port=MYSQL_PORT,
                                 charset='utf8')
            setStatus(db, 'article', 'dbcode=CAPJ&dbname=CAPJDAY&filename=JEXK20210511001')
        except:
            self.assertTrue(False, '设置状态位异常')

    def test_saveArticle(self):
        try:
            db = pymysql.connect(host=MYSQL_HOST, user=USERNAME, passwd=PASSWORD,
                                 db=DATABASE, port=MYSQL_PORT, charset='utf8')
            g = Graph(auth=('neo4j', '123456'))
            save_article(db, g)
            db.close()
        except:
            self.assertTrue(False, '存储文章节点neo4j异常')

    def test_setstatus_target(self):
        """状态位"""
        try:
            db = pymysql.connect(host=MYSQL_HOST, user=USERNAME, passwd=PASSWORD,
                                 db=DATABASE, port=MYSQL_PORT, charset='utf8')
            setstatus_target(db, 'article', 1)
            db.close()
        except:
            self.assertTrue(False, '将状态位置为0异常')

    def test_saveAuthor(self):
        try:
            db = pymysql.connect(host=MYSQL_HOST, user=USERNAME, passwd=PASSWORD,
                                 db=DATABASE, port=MYSQL_PORT, charset='utf8')
            g = Graph(auth=('neo4j', '123456'))
            save_author(db, g)
            db.close()
        except:
            self.assertTrue(False, '存储文章节点neo4j异常')


if __name__ == '__main__':
    unittest.main()
