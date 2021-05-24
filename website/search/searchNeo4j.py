from py2neo import Graph, NodeMatcher

from .ogm import Article, Author, Organization, Source

g = Graph(auth=('neo4j', '123456'))


def searchArticle(g, keyword):
    """检索关键词
    :return: 关键词文章列表
    """
    matcher = NodeMatcher(g)
    result = matcher.match("article").where("_.title =~'.*{}.*'".format(keyword))
    res = list(result)
    article_list = []
    for a in res:
        article = Article()
        article.title = a.get('title')
        article.url = a.get('url')
        article.summary = a.get('summary')
        date = str(a.get('date'))
        article.date = date[0:10]
        article_list.append(article)
    return article_list


def getArticleDetail(url):
    """获取文章详情"""
    matcher = NodeMatcher(g)
    m = matcher.match("article").where("_.url ='{}'".format(url))
    res = m.first()

    article = Article()
    if res:
        article.url = res.get('url')
        article.title = res.get('title')
        article.summary = res.get('summary')
        article.date = res.get('date').date()
        article.keywords = res.get('keywords')
    else:
        article.title = '空'
    return article


def getAuthorDetail(url):
    """获取作者详情"""
    matcher = NodeMatcher(g)
    m = matcher.match("author").where("_.url ='{}'".format(url))
    res = m.first()

    author = Author()
    if res:
        author.url = res.get('url')
        author.name = res.get('name')
        author.major = res.get('major')
        author.sum_download = res.get('sum_download')
        author.sum_publish = res.get('sum_publish')
    else:
        author.name = '无'
    return author


def getOrganizationDetail(url):
    """获取组织详情"""
    matcher = NodeMatcher(g)
    m = matcher.match("organization").where("_.url ='{}'".format(url))
    res = m.first()

    organization = Organization()
    if res:
        organization.url = res.get('url')
        organization.name = res.get('name')
        organization.region = res.get('region')
        organization.used_name = res.get('used_name')
        organization.website = res.get('website')
    else:
        organization.name = '无'
    return organization


def getSourceDetail(url):
    """获取文献来源url"""
    matcher = NodeMatcher(g)
    m = matcher.match("source").where("_.url ='{}'".format(url))
    res = m.first()
    source = Source()
    if res:
        source.url = res.get('url')
        source.name = res.get('name')
        source.basic_info = res.get('basic_info')
        source.publish_info = res.get('publish_info')
        source.evaluation = res.get('evaluation')
    else:
        source.name = '无'
    return source


def getAuO(url):
    """获取作者所在的组织"""
    res = []
    cql = 'MATCH (:author {url: "%s"})-[:组织]->(res) RETURN res' % url
    curr = g.run(cql)
    for c in curr.data():
        organization = Organization()
        organization.name = c.get('res').get('name')
        organization.url = c.get('res').get('url')
        organization.website = c.get('res').get('website')
        organization.region = c.get('res').get('region')
        organization.used_name = c.get('res').get('used_name')
        res.append(organization)
    return res


def getAus(url):
    """获取文章的作者列表"""
    res = []
    cql = 'MATCH (:article {url: "%s"})-[:作者]->(res) RETURN res' % url
    curr = g.run(cql)
    for c in curr.data():
        author = Author()
        author.name = c.get('res').get('name')
        author.url = c.get('res').get('url')
        author.major = c.get('res').get('major')
        author.sum_publish = c.get('res').get('sum_publish')
        author.sum_download = c.get('res').get('sum_download')
        res.append(author)
    return res


def getAStudents(url):
    """获取作者的学生"""
    res = []
    cql = 'MATCH (:author {url: "%s"})-[:学生]->(res) RETURN res' % url
    curr = g.run(cql)
    for c in curr.data():
        student = Author()
        student.name = c.get('res').get('name')
        student.url = c.get('res').get('url')
        student.major = c.get('res').get('major')
        student.sum_publish = c.get('res').get('sum_publish')
        student.sum_download = c.get('res').get('sum_download')
        res.append(student)
    return res


def getATeachers(url):
    """获取作者的导师"""
    res = []
    cql = 'MATCH (res:author)-[:学生]->(:author{url:"%s"}) RETURN res' % url
    curr = g.run(cql)
    for c in curr.data():
        teacher = Author()
        teacher.name = c.get('res').get('name')
        teacher.url = c.get('res').get('url')
        teacher.major = c.get('res').get('major')
        teacher.sum_publish = c.get('res').get('sum_publish')
        teacher.sum_download = c.get('res').get('sum_download')
        res.append(teacher)
    return res


def getAArticles(url):
    """作者发布的文章"""
    res = []
    cql = 'MATCH (res:article)-[:作者]->(:author{url:"%s"}) RETURN res' % url
    curr = g.run(cql)
    for c in curr.data():
        article = Article()
        article.url = c.get('res').get('url')
        article.title = c.get('res').get('title')
        article.keywords = c.get('res').get('keywords')
        article.summary = c.get('res').get('summary')
        article.date = c.get('res').get('date').date()
        res.append(article)
    return res


def getACo(url):
    """作者的同机构合作者"""
    # res.extend(getATeachers(url))
    # res.extend(getAStudents(url))
    co = []
    auOS = getAuO(url)
    if auOS:
        orURL = auOS[0].url
        co = getOAu(orURL)
    return co[0:20]


def getOAu(url):
    """获取机构的所有学者"""
    res = []
    cql = 'MATCH (res:author)-[r:`组织`]->(o:organization) where o.url="%s" RETURN res' % url
    curr = g.run(cql)
    for c in curr.data():
        author = Author()
        author.name = c.get('res').get('name')
        author.url = c.get('res').get('url')
        author.major = c.get('res').get('major')
        author.sum_publish = c.get('res').get('sum_publish')
        author.sum_download = c.get('res').get('sum_download')
        res.append(author)
    return res


def getReArticles(articlesUrl):
    """获取文章的相关文献"""
    article = getArticleDetail(articlesUrl)
    keywords = article.keywords
    keywords = keywords.replace(' ', '')
    keywords = keywords.split(',')
    res = []
    for key in keywords:
        # 搜索关键词相关的文章
        temp = searchArticle(g, key)
        res.extend(temp)
    return res


def getReAuthors(articleurl):
    """获取相关学者"""
    # 本篇文章的作者
    res = []
    authors = getAus(articleurl)
    for author in authors:
        co = getACo(author.url)
        # 同机构的学者
        res.extend(co)
    return res[0:20]


if __name__ == '__main__':
    # graph = Graph(auth=('neo4j', '123456'))
    # res = searchArticle(graph, '知识图谱')
    #
    # for r in res:
    #     print(r.title, r.url, r.date, r.summary)

    res = getAus('dbcode=CAPJ&dbname=CAPJDAY&filename=ZZDZ20210513000')
    for r in res:
        print(r.name)
