# 基于知识图谱的学术信息检索系统

本系统以知识图谱技术为基础，实现一个学术信息检索系统，主要实现学术信息定期爬取、学术信息更新、学术关联检索、知识化可视化界面等功能，分为服务器端和客户端两种用户。 服务器端可以在网站后台进行管理，用户通过Web界面在客户端自由检索信息。

**具体功能**

1. 服务器端：管理员可以对爬取信息、图数据库等进行添加、查看、修改或删除；
2. 客户端模块：学术信息检索；师生关系查询；领域知识检索；科研项目查询；学术论坛；学术信息管理。

```powershell
文件夹介绍

website 代码
resource 资源文件
```

## 功能实现

<p>
    <a href="https://www.anaconda.com/products/individual#Downloads"><img src="https://img.shields.io/badge/Anaconda3-4.10.1-44a833?logo=anaconda&style=flat" alt="Anaconda3"/></a>
    <a href="https://www.python.org/downloads/windows/"><img src="https://img.shields.io/badge/Python-3.8.10-3975a5?logo=python&style=flat" alt="Python"/></a>
    <a href="https://downloads.mysql.com/archives/community/"><img src="https://img.shields.io/badge/MySQL-5.7.29-f29111?logo=mysql&style=flat" alt="MySQL"/></a>
    <a href="https://we-yun.com/index.php/blog/releases-56.html"><img src="https://img.shields.io/badge/Neo4j-4.2.1-6dce9d?logo=neo4j&style=flat" alt="Neo4j"/></a>
    <a href="https://github.com/MicrosoftArchive/redis/releases"><img src="https://img.shields.io/badge/Redis-3.2.100-d72a20?logo=redis&style=flat" alt="Redis"/></a>
    <a href="https://magi.com/"><img src="https://img.shields.io/badge/magi.com-14a2f5" alt="magi.com"></a>
</p>


- [x] ~~爬取知网相关数据~~
- [ ] 前台控制爬虫
- [x] ~~后台管理系统~~
- [x] ~~构建知识图谱~~
- [x] ~~关键词检索~~
- [ ] 智能问答
- [x] ~~检索界面~~
- [ ] 图谱可视化
- [ ] 领域知识检索
- [ ] 科研项目查询
- [ ] 学术论坛

## 截图展示

<table>
    <tr>
        <td>爬虫1<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch1.jpg" alt="爬虫">
        </td>
        <td>爬虫2<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch2.jpg" alt="爬虫">
        </td>
    </tr>
    <tr>
        <td>数据库<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch3.jpg" alt="mysql">
        </td>
        <td>导入Neo4j<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch4.jpg" alt="toNeo4j">
        </td>
    </tr>
    <tr>
        <td>后台登录<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch5.jpg" alt="后台登录">
        </td>
        <td>后台管理<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch6.jpg" alt="后台管理">
        </td>
    </tr>
    <tr>
        <td>文献-作者<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch7.jpg" alt="Neo4j">
        </td>
        <td>学者-组织<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch8.jpg" alt="Neo4j">
        </td>
    </tr>
    <tr>
        <td>检索<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch9.jpg" alt="检索">
        </td>
        <td>文章详情<br/>
            <img src="https://cdn.jsdelivr.net/gh/eternidad33/picbed/img/docsearch10.jpg" alt="文章详情">
        </td>
    </tr>
</table>