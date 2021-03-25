import random
import re
import time

import pymysql

from crawl.cnki.spider.article import Article
from crawl.cnki.spider.author import Author
from crawl.cnki.spider.school import School


def save_article_mysql():
    """存储文章详情到article表中"""
    db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnki', port=3306, charset='utf8')
    curr = db.cursor()
    select_article_sql = 'select DISTINCT url_article from re_article_author;'
    articles = []
    try:
        # 获取所有文章
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


def save_author_mysql():
    """
    存储作者详情到 author表，
    存储师生关系到 re_teacher_student 关系表，
    存储作者所在学校到 re_author_school 关系表
    """
    db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnki', port=3306, charset='utf8')
    curr = db.cursor()
    # 获取要爬取的URL
    # select_author_sql = 'select DISTINCT url_author from re_article_author;'
    sqlc = "SELECT COUNT(DISTINCT a.url_student) FROM re_teacher_student as a WHERE a.url_student not in (SELECT url FROM " \
           "author) "
    curr.execute(sqlc)
    res = curr.fetchone()
    print("共需要爬取的作者信息个数为：", res[0])
    select_author_sql = "SELECT a.url_student FROM re_teacher_student as a WHERE a.url_student not in (SELECT url " \
                        "FROM author) "
    urls = []
    try:
        curr.execute(select_author_sql)
        result = curr.fetchall()
        for row in result:
            url_author = row[0]
            urls.append(url_author)
    except:
        print("不能获取到数据")

    c1, c2, c3 = 0, 0, 0
    for url in urls:
        try:
            author_spider = Author(url)
        except:
            print('不能打开网页')
            continue
        # 判断是否存在信息，不存在就插入url和name
        if not author_spider.hasInfo():
            m = re.search(r'skey=(.*?)&', url)
            temp = m.group(0)
            name = re.sub(r'(skey=)|&', '', temp)
            try:
                sql2 = "insert into author(url,name) values('{}','{}')".format(url, name)
                curr.execute(sql2)
                c1 += 1
                print('成功存储{}/{}'.format(c1, res[0]))
                print('【成功】{} 插入author表'.format(name))
            except Exception as e:
                print('插入表异常', e)
            continue
        name, major, sum_publish, sum_download, fields = author_spider.spBasic()
        sql1 = "insert into author(url,name, major, sum_publish, sum_download, fields) values('{}','{}','{}','{}'," \
               "'{}','{}')".format(url, name, major, sum_publish, sum_download, fields)
        try:
            curr.execute(sql1)
            db.commit()
            c1 += 1
            print('【成功】{}存储完成'.format(name))
        except Exception as e:
            print('存取异常,{}'.format(e))
            db.rollback()

        # 存储师生关系
        author_spider.crawl_teacher()
        author_spider.crawl_students()
        if author_spider.hasStudent:
            for surl in author_spider.students_url:
                sql2 = "insert into re_teacher_student(url_teacher,url_student) values('{}','{}')".format(url, surl)
                try:
                    curr.execute(sql2)
                    db.commit()
                    print('【成功】师生关系 {} 存储完成'.format(name))
                    c2 += 1
                except Exception as e:
                    print('存取异常,{}'.format(e))
                    db.rollback()
        if author_spider.hasTeacher:
            for turl in author_spider.teachers_url:
                sql3 = "insert into re_teacher_student(url_teacher,url_student) values('{}','{}')".format(turl, url)
                try:
                    curr.execute(sql3)
                    db.commit()
                    print('【成功】师生关系 {} 存储完成'.format(name))
                    c2 += 1
                except Exception as e:
                    print('存取异常,{}'.format(e))
                    db.rollback()

        # 存储作者所在学校url
        school_url = author_spider.spSchool()
        sql3 = "insert into re_author_school(url_author,url_school) values('{}','{}')".format(url, school_url)
        try:
            curr.execute(sql3)
            db.commit()
            print("【成功】{}所在学校存储完成".format(name))
            c3 += 1
        except Exception as e:
            print('存取异常,{}'.format(e))
            db.rollback()

        author_spider.close_driver()

    print('成功存储{}个作者'.format(c1))
    print('成功存储{}个师生关系'.format(c2))
    print('成功存储{}个所在学校链接'.format(c3))
    db.close()


def save_school():
    """存储作者所在学校的详情"""
    db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnki', port=3306, charset='utf8')
    curr = db.cursor()
    sqlc = "SELECT COUNT(DISTINCT url_school)FROM re_author_school where url_school not in (SELECT url from school)"
    curr.execute(sqlc)
    res = curr.fetchone()
    print("共需要爬取的学校个数为：", res[0])
    urls = []
    index, length = 0, 5
    try:
        sql1 = "SELECT DISTINCT url_school FROM re_author_school where url_school not in (SELECT url from school)"
        curr.execute(sql1)
        result = curr.fetchall()
        for row in result:
            url_school = row[0]
            urls.append(url_school)
    except:
        print("不能获取到数据")

    for url in urls:
        print('正在爬取：https://kns.cnki.net/kcms/detail/knetsearch.aspx?' + url)
        school_spider = School(url)
        name, name_used, region, official_website = school_spider.crawl()
        sql2 = "insert into school(url,name, name_used, region, official_website) values('{}','{}','{}','{}','{}')".format(
            url, name, name_used, region, official_website)
        try:
            curr.execute(sql2)
            db.commit()
            print("【成功】学校{}存储完成".format(name))
        except Exception as e:
            print('存取异常,{}'.format(e))
            db.rollback()
        # 随机等待1-3秒
        rand = random.randint(1, 3)
        time.sleep(rand)


def save_source_mysql():
    """存储文献来源
    判断文献类型，论文，期刊
    论文存储到 source_school 表
    期刊存储到 source_journal 表
    """
    # TODO 存储文献来源
    pass


if __name__ == '__main__':
    start = time.time()
    # save_author_mysql()
    save_school()
    end = time.time()
    t = end - start
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    print("程序耗时 {:.0f}时 {:.0f}分 {:.0f}秒".format(h, m, s))
