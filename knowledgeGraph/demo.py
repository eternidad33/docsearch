import csv

from py2neo import Graph, Node

from handle.entity.article import Article
from handle.entity.author import Author
from handle.entity.school import School

# 初始化图数据库
g = Graph(auth=('neo4j', '123456'))
g.run('match(n) detach delete n')

print('【neo4j】开始存储文章节点')
f_article = open('../crawl/cnki/csv/article.csv', encoding='utf-8')
reader_article = csv.reader(f_article)
header_1 = next(reader_article)
for row in reader_article:
    # row为每一行元素
    if len(row) == 9:
        # print(row)
        article = Article()
        article.title = row[0]
        article.authors = row[1]
        article.summary = row[2]
        article.keys = row[3]
        article.funds = row[4]
        article.doi = row[5]
        article.album = row[6]
        article.special = row[7]
        article.classNo = row[8]
        node = Node('Article', 标题=article.title, 作者=article.authors, 摘要=article.summary, 关键词=article.keys,
                    资助机构=article.funds, doi=article.doi, 专辑=article.album, 专题=article.special, 分类号=article.classNo)
        g.create(node)
print('【neo4j】所有文章节点存储完毕\n')

print('【neo4j】开始存储作者节点')
f_author = open('../crawl/cnki/csv/author.csv', encoding='utf-8')
reader_author = csv.reader(f_author)
header_2 = next(reader_author)
for row in reader_author:
    if len(row) == 9:
        # 姓名, 学校, 专业, 总发布量, 总下载量, 专注领域, 作者文献, 导师, 学生
        author = Author()
        author.name = row[0]
        author.school = row[1]
        author.major = row[2]
        author.sum_publish = row[3]
        author.sum_download = row[4]
        author.fields = row[5]
        author.articles = row[6]
        author.teacher = row[7]
        author.students = row[8]
        node = Node('Author', 姓名=author.name, 学校=author.school, 专业=author.major, 总发布量=author.sum_publish,
                    总下载量=author.sum_download, 专注领域=author.fields, 作者文献=author.articles, 导师=author.teacher,
                    学生=author.students)
        g.create(node)
print('【neo4j】所有作者节点存储完毕\n')

print('【neo4j】开始存储学校节点')
f_school = open('../crawl/cnki/csv/school.csv', encoding='utf-8')
reader_school = csv.reader(f_school)
header_3 = next(reader_school)
for row in reader_school:
    if len(row) == 4:
        school = School()
        # 名称, 曾用名, 地域, 官网
        school.name = row[0]
        school.name_used = row[1]
        school.region = row[2]
        school.official_website = row[3]
        node = Node('School', 名称=school.name, 曾用名=school.name_used, 地域=school.region, 官网=school.official_website)
        g.create(node)
print('【neo4j】所有学校节点存储完毕\n')
