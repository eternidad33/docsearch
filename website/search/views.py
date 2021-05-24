# Create your views here.
from django.shortcuts import render

from .searchNeo4j import *

g = Graph(auth=('neo4j', '123456'))


def index(request):
    return render(request, 'search/index.html')


def search(request, keyword):
    articles = searchArticle(g, '知识图谱')
    return render(request, 'search/results.html', {'articles': articles})


def articleDetail(request, articleurl):
    # print(articleurl)
    article = getArticleDetail(articleurl)
    authors = getAus(articleurl)
    # 相关文章
    reArticles = getReArticles(articleurl)[0:7]
    # 相关学者
    reAuthors = getReAuthors(articleurl)
    return render(request, 'search/article.html',
                  {'article': article, 'authors': authors, 'reArticles': reArticles, 'reAuthors': reAuthors})


def authorDetail(request, authorurl):
    author = getAuthorDetail(authorurl)
    res = getAuO(authorurl)
    organization = res[0] if len(res) > 0 else Organization()
    # 导师
    teachers = getATeachers(authorurl)
    # 学生
    students = getAStudents(authorurl)
    # 发布的文章
    articles = getAArticles(authorurl)
    # 同机构的合作者
    co = getACo(authorurl)
    return render(request, 'search/author.html',
                  {'author': author, 'organization': organization, 'articles': articles, 'teachers': teachers,
                   'students': students, 'co': co})


def organizationDetail(request, organizationUrl):
    organization = getOrganizationDetail(organizationUrl)
    authors = getOAu(organizationUrl)[0:100]
    return render(request, 'search/organization.html', {'organization': organization, 'authors': authors})


def sourceDetail(request, sourceUrl):
    source = getSourceDetail(sourceUrl)
    return render(request, 'search/source.html', {'source': source})
