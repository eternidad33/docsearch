import re

import pymysql

from crawl.cnki.spider.article import Article

db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnki', port=3306, charset='utf8')
curr = db.cursor()
select_article_sql = 'select DISTINCT url_article from re_article_author;'
select_author_sql = 'select DISTINCT url_author from re_article_author;'
# 获取所有文章
curr.execute(select_article_sql)
articles = []
try:
    curr.execute(select_article_sql)
    result = curr.fetchall()
    for row in result:
        url_article = row[0]
        articles.append(url_article)
except:
    print("不能获取到数据")
c = 0
for a in articles:
    article = Article(a)
    title, summary, keys, funds, doi, album, special, classNo = article.spider()
    sql_insert_article = "insert into article(url,title, summary, keyss, funds, doi, album, special, classNo) values(" \
                         "'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a, title, summary, keys, funds, doi,
                                                                                album, special, classNo)
    try:
        curr.execute(sql_insert_article)
        db.commit()
        print('【存储成功】%s' % title)
        c += 1
    except Exception as e:
        print('文献【{}】存取异常,{}'.format(title, e))
        db.rollback()
print('成功存储{}条记录'.format(c))
db.close()
