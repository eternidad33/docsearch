from py2neo import Relationship
from py2neo.matching import *

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "cnkidemo"

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379


def setStatus_re(db, table, key1, key2, value1, value2, status):
    """设置关系表的状态位"""
    sql = "UPDATE {} SET status={} WHERE {}='{}' and {}='{}'".format(table, status, key1, key2, value1, value2)
    currsor = db.cursor()
    try:
        currsor.execute(sql)
        db.commit()
        print('表{},行{}---{}的状态位{}设置成功'.format(table, value1, value2, status))
    except:
        print('表{},行{}---{}的状态位{}设置失败'.format(table, value1, value2, status))


def setStatus(db, table, rowID, status):
    """设置状态位"""
    sql = "UPDATE {} SET status={} WHERE url='{}'".format(table, status, rowID)
    currsor = db.cursor()
    try:
        currsor.execute(sql)
        db.commit()
        print('表{},行{}的状态位设置{}成功'.format(table, rowID, status))
    except:
        print('表{},行{}的状态位设置{}失败'.format(table, rowID, status))


def save_article(db, graph):
    """存储文章节点"""
    print("正在存储文章节点，请稍等...")
    sql = 'SELECT url, title, summary, keywords,date ' \
          'FROM article where status=0'
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail = 0, 0
    for row in rows:
        try:
            url = row[0]
            title = row[1]
            summary = row[2]
            keywords = row[3]
            date = row[4]
            node = Node('article', url=url, title=title, summary=summary, keywords=keywords, date=date)
            graph.create(node)
            print("{}成功导入neo4j".format(title))
            # 设置此行状态位为1
            setStatus(db, 'article', url, 1)
            success += 1
        except Exception as e:
            print('【失败】存储文章节点', e)
            setStatus(db, 'article', url, 2)
            fail += 1
    print('所有文章节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_author(db, graph):
    """存储作者节点"""
    print("正在存储作者节点，请稍等...")
    sql = 'SELECT url, name, major, sum_publish, sum_download ' \
          'FROM author where status=0'
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail = 0, 0
    for row in rows:
        try:
            url = row[0]
            name = row[1]
            major = row[2]
            sum_publish = row[3]
            sum_download = row[4]
            node = Node('author', url=url, name=name, major=major,
                        sum_publish=sum_publish, sum_download=sum_download)
            graph.create(node)
            print("{}成功导入neo4j".format(name))
            # 设置此行状态位为1
            setStatus(db, 'author', url, 1)
            success += 1
        except Exception as e:
            print('【失败】存储作者节点', e)
            setStatus(db, 'author', url, 2)
            fail += 1
    print('所有作者节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def setstatus_target(db, table, target):
    """将实体表中的所有状态位设置为target"""
    sql = "SELECT url from {} where status != {}".format(table, target)
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        url = row[0]
        setStatus(db, table, url, target)
        print('【成功】状态位置{},{}'.format(target, url))


def setStatus0_re(db, table, name1, name2):
    """将关系表中所有数据设为0"""
    sql = ""


def save_re_article_author(db, graph):
    """存储文献作者关系"""
    print("正在存储文献作者关系，请稍等...")
    sql = 'SELECT url_article,url_author ' \
          'FROM re_article_author where status=0'
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail = 0, 0
    for row in rows:
        match = NodeMatcher(graph)
        url_article = row[0]
        url_author = row[1]
        try:
            # 查找文章节点
            node_article = match.match('Article').where('_.url="{}"'.format(url_article)).first()
            # 查找作者节点
            node_author = match.match('Author').where('_.url="{}"'.format(url_author)).first()
            # 建立关系
            if node_article and node_author:
                re = Relationship(node_article, '作者', node_author)
                graph.create(re)
                setStatus_re(db, 're_article_author', url_article, url_author)
                success += 1
            else:
                fail += 1
        except Exception as e:
            print('【失败】文章作者关系', e)

    print('所有文献作者关系存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))
