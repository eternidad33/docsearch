import time

import pymysql
from py2neo import Graph, Relationship
from py2neo.matching import *


def save_article(cursor, graph):
    """存储文章节点
    :param cursor: mysql 游标对象
    :param graph: neo4j 数据库连接
    """
    print("正在存储文章节点，请稍等...")
    sql = 'SELECT url, title, summary, keyss, funds, doi, album, special, classNo FROM article'
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail = 0, 0
    for row in rows:
        try:
            url = row[0]
            title = row[1]
            summary = row[2]
            keys = row[3]
            funds = row[4]
            doi = row[5]
            album = row[6]
            special = row[7]
            classNo = row[8]
            node = Node('Article', url=url, title=title, summary=summary, keys=keys, funds=funds, doi=doi, album=album,
                        special=special, classNo=classNo)
            graph.create(node)
            success += 1
        except Exception as e:
            print('【失败】存储文章节点', e)
            fail += 1
    print('所有文章节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_author(cursor, graph):
    """存储作者节点
    :param cursor: mysql 游标对象
    :param graph: neo4j 数据库连接
    """
    print("正在存储作者节点，请稍等...")
    sql = 'SELECT url, name, major, sum_publish, sum_download, fields FROM author'
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
            fields = row[5]
            node = Node('Author', url=url, name=name, major=major, sum_publish=sum_publish, sum_download=sum_download,
                        fields=fields)
            graph.create(node)
            success += 1
        except Exception as e:
            print('【失败】存储作者节点', e)
            fail += 1
    print('所有作者节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_school(cursor, graph):
    """存储学校
    :param cursor: mysql 游标对象
    :param graph: neo4j 数据库连接
    """
    print("正在存储学校节点，请稍等...")
    sql = 'SELECT url, name, name_used, region, official_website FROM school'
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail = 0, 0
    for row in rows:
        try:
            url = row[0]
            name = row[1]
            name_used = row[2]
            region = row[3]
            official_website = row[4]
            node = Node('School', url=url, name=name, name_used=name_used, region=region,
                        official_website=official_website)
            graph.create(node)
            success += 1
        except Exception as e:
            print('【失败】存储学校节点', e)
            fail += 1
    print('所有学校节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_journal(cursor, graph):
    """存储期刊
    :param cursor: mysql 游标对象
    :param graph: neo4j 数据库连接
    """
    print("正在存储文献来源节点，请稍等...")
    sql = 'SELECT url, name, name_en, journals, basic_info, album, special, count_publish FROM source_journal'
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail = 0, 0
    for row in rows:
        try:
            url = row[0]
            name = row[1]
            name_en = row[2]
            journals = row[3]
            basic_info = row[4]
            album = row[5]
            special = row[6]
            count_publish = row[7]
            node = Node('Source', url=url, name=name, name_en=name_en, journals=journals, basic_info=basic_info,
                        album=album, special=special, count_publish=count_publish)
            graph.create(node)
            success += 1
        except Exception as e:
            print('【失败】存储文献来源节点', e)
            fail += 1
    print('所有文献来源节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_re_article_author(cursor, graph):
    """存储文献作者关系
    :param cursor: mysql 游标对象
    :param graph: neo4j 数据库连接
    """
    print("正在存储文献作者关系，请稍等...")
    sql = 'SELECT url_article,url_author FROM re_article_author'
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
                success += 1
            else:
                fail += 1
        except Exception as e:
            print('【失败】文章作者关系', e)

    print('所有文献作者关系存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_re_article_source(cursor, graph):
    """存储文献与来源的关系
    :param cursor: mysql 游标对象
    :param graph: neo4j 数据库连接
    """
    print("正在存储文献来源关系，请稍等...")
    sql = 'SELECT url_article,url_source FROM re_article_source'
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail = 0, 0
    for row in rows:
        match = NodeMatcher(graph)
        url_article = row[0]
        url_source = row[1]
        try:
            # 查找文章节点
            node_article = match.match('Article').where('_.url="{}"'.format(url_article)).first()
            # 查找来源节点
            node_source = match.match('Source').where('_.url="{}"'.format(url_source)).first()
            # 建立关系
            if node_article and node_source:
                re = Relationship(node_article, '来源', node_source)
                graph.create(re)
                success += 1
            else:
                fail += 1
        except Exception as e:
            print('【失败】文章来源关系', e)

    print('所有文献来源关系存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_re_author_school(cursor, graph):
    """存储作者与学校的关系
    :param cursor: mysql 游标对象
    :param graph: neo4j 数据库连接
    """
    print("正在存储作者学校关系，请稍等...")
    sql = 'SELECT url_author,url_school FROM re_author_school'
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail = 0, 0
    for row in rows:
        match = NodeMatcher(graph)
        url_author = row[0]
        url_school = row[1]
        try:
            # 查找作者节点
            node_author = match.match('Author').where('_.url="{}"'.format(url_author)).first()
            # 查找学校节点
            node_school = match.match('School').where('_.url="{}"'.format(url_school)).first()
            # 建立关系
            if node_author and node_school:
                re = Relationship(node_author, '学校', node_school)
                graph.create(re)
                success += 1
            else:
                fail += 1
        except Exception as e:
            print('【失败】作者学校关系', e)

    print('所有作者学校关系存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_re_tea_stu(cursor, graph):
    """存储师生关系
    :param cursor: mysql 游标对象
    :param graph: neo4j 数据库连接
    """
    print("正在存储师生关系，请稍等...")
    sql = 'SELECT url_teacher,url_student FROM re_teacher_student'
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail = 0, 0
    for row in rows:
        match = NodeMatcher(graph)
        url_teacher = row[0]
        url_student = row[1]
        try:
            # 查找老师节点
            node_tea = match.match('Author').where('_.url="{}"'.format(url_teacher)).first()
            # 查找作者节点
            node_stu = match.match('Author').where('_.url="{}"'.format(url_student)).first()
            # 建立关系
            if node_tea and node_stu:
                re = Relationship(node_tea, '学生', node_stu)
                graph.create(re)
                success += 1
            else:
                fail += 1
        except Exception as e:
            print('【失败】师生关系', e)

    print('所有师生关系存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


if __name__ == '__main__':
    print('主程序开始执行，当前时间：{}\n'.format(time.strftime('%H:%M:%S', time.localtime())))
    start = time.time()

    db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnki', port=3306, charset='utf8')
    curr = db.cursor()
    # 初始化图数据库
    g = Graph(auth=('neo4j', '123456'))
    g.run('match(n) detach delete n')
    save_article(curr, g)
    save_author(curr, g)
    save_school(curr, g)
    save_journal(curr, g)
    save_re_article_author(curr, g)
    save_re_article_source(curr, g)
    save_re_author_school(curr, g)
    save_re_tea_stu(curr, g)
    db.close()

    end = time.time()
    t = end - start
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    print("程序耗时 {:.0f}时 {:.0f}分 {:.0f}秒".format(h, m, s))
