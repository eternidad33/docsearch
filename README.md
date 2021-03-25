# 学术信息检索系统

本系统以知识图谱技术为基础，实现一个学术信息检索系统，主要实现学术信息定期爬取、学术信息更新、学术关联检索、知识化可视化界面等功能，分为服务器端和客户端两种用户。
服务器端可以在网站后台进行管理，用户通过Web界面在客户端自由检索信息。

**具体功能**

1. 服务器端：管理员可以对爬取信息、图数据库等进行添加、查看、修改或删除；
2. 客户端模块：学术信息检索；师生关系查询；领域知识检索；科研项目查询；学术论坛；学术信息管理。

**目标**

完成系统中的主要功能设计。

**要求**

1. 学会利用爬虫技术爬取Web信息；
2. 利用自然语言处理技术提取学术信息；
3. 利用图数据库存储三元组知识；
4. 利用知识图谱技术的SPARQL语言完成图数据的检索任务。

## 爬虫

- [x] 简单爬取单个页面信息

- [x] 存入CSV

- [x] mysql 存储数据关系

  ![](https://gitee.com/eternidad33/picbed/raw/master/img/QQ截图20210325213045.jpg)

- [ ] 多线程

- [ ] 动态 ip，headers

- [ ] 定时爬取

## 数据分析

- [x] 去掉 mysql 冗余的数据

  ```sql
  -- 删除重复数据并保留id最小的一个 
  DELETE FROM author
  WHERE NAME IN ( SELECT NAME 
                 FROM ( SELECT NAME 
                       FROM author 
                       GROUP BY NAME 
                       HAVING COUNT(NAME) > 1) a
                )
  -- 排除最小的id
  AND id NOT IN (
  	SELECT id
  	FROM (SELECT min(id) AS id
            FROM author 
            GROUP BY NAME 
            HAVING count(NAME) > 1 ) b
  )
  ```

## 知识图谱

- [x] 简单的知识图谱Demo

  ![](https://gitee.com/eternidad33/picbed/raw/master/img/火狐截图_2021-03-25T13-11-34.549Z.png)

- [ ] 检索系统

## Web可视化

- [ ] 简单的web界面
- [ ] echarts 设计关系图