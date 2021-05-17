from py2neo import Relationship
from py2neo.matching import *


def setStatus_re(db, table, key1, key2, value1, value2, status):
    """设置关系表的状态位"""
    sql = "UPDATE {} SET status={} WHERE {}='{}' and {}='{}'".format(table, status, key1, value1, key2, value2)
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


def setStatusRE_target(db, table, name1, name2, target):
    """将关系表中所有数据设为target"""
    sql = "SELECT {},{} from {} where status != {}".format(name1, name2, table, target)
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        value1 = row[0]
        value2 = row[1]
        setStatus_re(db, table, name1, name2, value1, value2, target)
        print('【成功】状态位置{},{}---{}'.format(target, value1, value2))


def setCONSTRAINT(graph, label, attribute):
    """创建唯一索引
    :param graph: neo4j连接
    :param label: 标签
    :param attribute: 属性
    """
    cql = 'CREATE CONSTRAINT ON (n:{}) ASSERT n.{} IS UNIQUE'.format(label, attribute)
    graph.run(cql)


def save_article(db, graph):
    """存储文章节点"""
    print("正在存储文章节点，请稍等...")
    sql = 'SELECT url, title, summary, keywords,date ' \
          'FROM article where status =0'
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail, count, length = 0, 0, 0, len(rows)
    print('共需存储{}个文章'.format(length))
    for row in rows:
        count += 1
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

        print("已完成 {} / {}".format(count, length))
    print('所有文章节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_author(db, graph):
    """存储作者节点"""
    print("正在存储作者节点，请稍等...")
    sql = 'SELECT url, name, major, sum_publish, sum_download ' \
          'FROM author where status =0'
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail, count, length = 0, 0, 0, len(rows)
    print('共需存储{}个作者'.format(length))
    for row in rows:
        count += 1
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

        print("已完成 {} / {}".format(count, length))
    print('所有作者节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_source(db, graph):
    """存储文献来源节点"""
    print("正在存储文献来源节点，请稍等...")
    sql = 'SELECT url ,name,basic_info,publish_info,evaluation ' \
          'FROM source where status =0'
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail, count, length = 0, 0, 0, len(rows)
    print('共需存储{}个文献来源'.format(length))
    for row in rows:
        count += 1
        try:
            url = row[0]
            name = row[1]
            basic_info = row[2]
            publish_info = row[3]
            evaluation = row[4]
            node = Node('source', url=url, name=name, basic_info=basic_info,
                        publish_info=publish_info, evaluation=evaluation)
            graph.create(node)
            print("{}成功导入neo4j".format(name))
            # 设置此行状态位为1
            setStatus(db, 'source', url, 1)
            success += 1
        except Exception as e:
            print('【失败】存储文献来源节点', e)
            setStatus(db, 'source', url, 2)
            fail += 1

        print("已完成 {} / {}".format(count, length))
    print('所有文献来源节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_organization(db, graph):
    """存储组织节点"""
    print("正在存储组织节点，请稍等...")
    sql = 'SELECT url ,name,used_name,region,website ' \
          'FROM organization where status =0'
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail, count, length = 0, 0, 0, len(rows)
    print('共需存储{}个组织'.format(length))
    for row in rows:
        count += 1
        try:
            url = row[0]
            name = row[1]
            used_name = row[2]
            region = row[3]
            website = row[4]
            node = Node('organization', url=url, name=name, used_name=used_name,
                        region=region, website=website)
            graph.create(node)
            print("{}成功导入neo4j".format(name))
            # 设置此行状态位为1
            setStatus(db, 'organization', url, 1)
            success += 1
        except Exception as e:
            print('【失败】存储组织节点', e)
            setStatus(db, 'organization', url, 2)
            fail += 1

        print("已完成 {} / {}".format(count, length))
    print('所有组织节点存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_re_article_author(db, graph):
    """存储文献作者关系"""
    print("正在存储文献作者关系，请稍等...")
    sql = 'SELECT url_article,url_author ' \
          'FROM re_article_author where status=0'
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail, count, length = 0, 0, 0, len(rows)
    for row in rows:
        count += 1
        match = NodeMatcher(graph)
        url_article = row[0]
        url_author = row[1]
        try:
            # 查找文章节点
            node_article = match.match('article').where('_.url="{}"'.format(url_article)).first()
            # 查找作者节点
            node_author = match.match('author').where('_.url="{}"'.format(url_author)).first()
            # 建立关系
            if node_article and node_author:
                re = Relationship(node_article, '作者', node_author)
                graph.create(re)
                setStatus_re(db, 're_article_author', 'url_article', 'url_author', url_article, url_author, 1)
                success += 1
            else:
                fail += 1
                setStatus_re(db, 're_article_author', 'url_article', 'url_author', url_article, url_author, 2)
        except Exception as e:
            fail += 1
            setStatus_re(db, 're_article_author', 'url_article', 'url_author', url_article, url_author, 3)
            print('【失败】文章作者关系', e)

        print("已完成 {} / {}".format(count, length))

    print('所有文献作者关系存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_re_article_source(db, graph):
    print("正在存储文献来源关系，请稍等...")
    table_name = "re_article_source"
    name1 = "url_article"
    name2 = "url_source"
    node1 = 'article'
    node2 = 'source'
    relation = '来源'
    sql = 'SELECT {},{} FROM {} where status=0'.format(name1, name2, table_name)
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail, count, length = 0, 0, 0, len(rows)
    for row in rows:
        count += 1
        match = NodeMatcher(graph)
        url_article = row[0]
        url_source = row[1]
        try:
            # 查找文章节点
            node_article = match.match(node1).where('_.url="{}"'.format(url_article)).first()
            # 查找来源节点
            node_source = match.match(node2).where('_.url="{}"'.format(url_source)).first()
            # 建立关系
            if node_article and node_source:
                re = Relationship(node_article, relation, node_source)
                graph.create(re)
                setStatus_re(db, table_name, name1, name2, url_article, url_source, 1)
                success += 1
            else:
                fail += 1
                setStatus_re(db, table_name, name1, name2, url_article, url_source, 2)
        except Exception as e:
            fail += 1
            setStatus_re(db, table_name, name1, name2, url_article, url_source, 3)
            print('【失败】文章来源关系', e)

        print("已完成 {} / {}".format(count, length))

    print('所有文献来源关系存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_re_author_organization(db, graph):
    print("正在存储作者组织关系，请稍等...")
    table_name = "re_author_organization"
    name1 = "url_author"
    name2 = "url_organization"
    node1 = 'author'
    node2 = 'organization'
    relation = '组织'
    sql = 'SELECT {},{} FROM {} where status=0'.format(name1, name2, table_name)
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail, count, length = 0, 0, 0, len(rows)
    for row in rows:
        count += 1
        match = NodeMatcher(graph)
        url_author = row[0]
        url_organization = row[1]
        try:
            node_author = match.match(node1).where('_.url="{}"'.format(url_author)).first()
            node_organization = match.match(node2).where('_.url="{}"'.format(url_organization)).first()
            # 建立关系
            if node_author and node_organization:
                re = Relationship(node_author, relation, node_organization)
                graph.create(re)
                setStatus_re(db, table_name, name1, name2, url_author, url_organization, 1)
                success += 1
            else:
                fail += 1
                setStatus_re(db, table_name, name1, name2, url_author, url_organization, 2)
        except Exception as e:
            fail += 1
            setStatus_re(db, table_name, name1, name2, url_author, url_organization, 3)
            print('【失败】作者组织关系', e)

        print("已完成 {} / {}".format(count, length))

    print('所有作者组织关系存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def save_re_teacher_student(db, graph):
    print("正在存储师生关系，请稍等...")
    table_name = "re_teacher_student"
    name1 = "url_teacher"
    name2 = "url_student"
    node1 = 'author'
    node2 = 'author'
    relation = '学生'
    sql = 'SELECT {},{} FROM {} where status=0'.format(name1, name2, table_name)
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    success, fail, count, length = 0, 0, 0, len(rows)
    for row in rows:
        count += 1
        match = NodeMatcher(graph)
        url_teacher = row[0]
        url_student = row[1]
        try:
            node_teacher = match.match(node1).where('_.url="{}"'.format(url_teacher)).first()
            node_student = match.match(node2).where('_.url="{}"'.format(url_student)).first()
            # 建立关系
            if node_teacher and node_student:
                re = Relationship(node_teacher, relation, node_student)
                graph.create(re)
                setStatus_re(db, table_name, name1, name2, url_teacher, url_student, 1)
                success += 1
            else:
                fail += 1
                setStatus_re(db, table_name, name1, name2, url_teacher, url_student, 2)
        except Exception as e:
            fail += 1
            setStatus_re(db, table_name, name1, name2, url_teacher, url_student, 3)
            print('【失败】师生关系', e)

        print("已完成 {} / {}".format(count, length))

    print('所有师生关系存储完毕，成功存储{}个，失败{}个\n'.format(success, fail))


def main(db, graph):
    save_article(db, graph)
    save_author(db, graph)
    save_source(db, graph)
    save_organization(db, graph)
    save_re_article_author(db, graph)
    save_re_article_source(db, graph)
    save_re_teacher_student(db, graph)
    save_re_author_organization(db, graph)
