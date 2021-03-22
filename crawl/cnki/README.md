## 知网相关URL解析

### 文献详情URL解析

**期刊文献**，例如，[TransPath:一种基于深度迁移强化学习的知识推理方法](https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CAPJ&dbname=CAPJLAST&filename=XXWX2021031700R)

这个链接`https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CAPJ&dbname=CAPJLAST&filename=XXWX2021031700R`可进入文章详情

这个是通过selenium获取到的`https://kns.cnki.net/KNS8/Detailsfield=fn&QueryID=0&CurRec=1&recid=&FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ&yx=Y&pr=&URLID=21.1106.TP.20210319.1034.020`但是点击进去就不能获取到文章详情😐

通过分析两个URL可以发现，只需通过正则表达式提取出`FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ`这一部分然后拼接成`https://kns.cnki.net/kcms/detail/detail.aspx?FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ`同样可以进入文章详情

正则表达式：`FileName=(.*?)&DbName=(.*?)&DbCode=(.*?)&`

**外文期刊**：例如，[An ontology-based deep learning approach for triple classification with out-of-knowledge-base entities](https://kns.cnki.net/KNS8/Detail/RedirectScholar?flag=TitleLink&tablename=SJESLAST&filename=SJES2F9E9C8E8C8C9961EF1F032D1ACD3037)

可以直接通过slenium获取到的URL进入文章详情页

**论文文献**：例如，[基于大数据的智能辅助诊疗全流程管理系统的研究与实现](https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFDTEMP&filename=1020431527.nh)

URL获取过程和**期刊文献**类似



### 作者详情URL解析

例如，[崔员宁]()

可进入详情的链接，`https://kns.cnki.net/kcms/detail/knetsearch.aspx?dbcode=CAPJ&sfield=au&skey=%e5%b4%94%e5%91%98%e5%ae%81&code=43931005`

通过selenium获取的URL为`https://kns.cnki.net/KNS8/Detail?sdb=CAPJ&sfield=%e4%bd%9c%e8%80%85&skey=%e5%b4%94%e5%91%98%e5%ae%81&scode=43931005&acode=4393100`

这个链接解析起来有点复杂

固定部分：`https://kns.cnki.net/kcms/detail/knetsearch.aspx?`

dbcode：`dbcode=`+ 获取 href 的 sdb 值

skey：`&sfield=au&skey=`+ 获取 href 的 skey 值

code：`&code=`+ 获取 href 的 acode 值

```python
def href_to_url(href):
    baseURL = 'https://kns.cnki.net/kcms/detail/knetsearch.aspx?'
    m1 = re.search(r'sdb=(.*?)&', href)
    m2 = re.search(r'skey=(.*?)&', href)
    m3 = re.search(r'acode=.*', href)
    dbcode = m1.group(0).replace('sdb=', '')
    skey = m2.group(0).replace('skey=', '')
    code = m3.group(0).replace('acode=', '')
    return '{}dbcode={}sfield=au&skey={}code={}'.format(baseURL, dbcode, skey, code)
```

### 作者所在学校URL解析





### 文献来源URL详情



## 重构

之前是把爬取的数据暂存到了URL，这次把数据先存到mysql中，重构后的E-R图需要用到5个实体表，4个关系表。

- 实体表：文章，作者，学校，论文所在学校，期刊机构
- 关系表：文章-作者，师生关系，文章-来源，作者-学校

E-R图如下所示：

![](https://gitee.com/eternidad33/picbed/raw/master/img/24ad65wd2a23s1d.png)