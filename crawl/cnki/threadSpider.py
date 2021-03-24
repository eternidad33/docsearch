import threading

import pymysql

from crawl.cnki.spider.article import Article


class article_spider(threading.Thread):
    def __init__(self, url):
        super(article_spider, self).__init__()
        self.url = url
        # 创建数据库连接
        self.db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnki', port=3306, charset='utf8')
        self.curr = self.db.cursor()

    def run(self) -> None:
        self.db.close()

    def crawl(self):
        """
        爬取文章信息
        """
        pass
