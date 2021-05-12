import re


def organizationToUrl(href):
    """将作者机构字符串转换为相应链接
    例如："\n                        TurnPageToKnet('in','南京邮电大学','0101257')\n
    转换成 “sfield=in&skey=南京邮电大学&code=0101257”
    """
    start, end = href.index('(') + 1, href.index(')')
    s = href[start:end]
    list0 = s.replace("'", "").split(',')
    res = "sfield=" + list0[0] + "&skey=" + list0[1] + "&code=" + list0[2]
    return res


def stuToUrl(href):
    """
    将('au','王永超','42141239')
    转换成 sfield=au&skey=王永超&code=42141239
    访问链接：https://kns.cnki.net/kcms/detail/knetsearch.aspx?+返回值
    """
    ss = href.split(',')
    m1 = re.search(r"'(.*?)'", ss[0])
    m2 = re.search(r"'(.*?)'", ss[1])
    m3 = re.search(r"'(.*?)'", ss[2])
    sfield = m1.group(0).replace("'", "")
    skey = m2.group(0).replace("'", "")
    code = m3.group(0).replace("'", "")

    return 'sfield={}&skey={}&code={}'.format(sfield, skey, code)


def articleToUrl(href):
    """将关键词列表的文章url转换成相应的字符串
    例如：'https://kns.cnki.net/KNS8/Detail?sfield=fn&QueryID=5&CurRec=1&DbCode=CAPJ&dbname=CAPJDAY&filename=KQDX20210511000&urlid=51.1192.TK.20210511.1126.002&yx=Y'
    返回：dbcode=CAPJ&dbname=CAPJDAY&filename=KQDX20210511000&
    """
    res = '#'
    try:
        href = href.upper()
        m0 = re.search(r"DBCODE=(.*?)&", href)
        m1 = re.search(r'DBNAME=(.*?)&', href)
        m2 = re.search(r'FILENAME=(.*?)&', href)
        dbcode = m0.group(1)
        dbname = m1.group(1)
        filename = m2.group(1)
        res = 'dbcode=' + dbcode + '&dbname=' + dbname + '&filename=' + filename
    except Exception as e:
        res = '#'
    return res


def extractAuthorCode(href):
    """抽取检索页作者href中的code值
    例如：https://kns.cnki.net/KNS8/Detail?sdb=CJFQ&sfield=%e4%bd%9c%e8%80%85&skey=%e8%b5%b5%e6%9a%be&scode=44906811&acode=44906811
    返回 44906811&
    """
    try:
        href = href.lower()
        m0 = re.search(r'scode=(.*?)&', href)
        res = m0.group(1)
    except Exception as e:
        res = '#'
    return res


def sourceToUrl(href):
    """检索页文献来源href
    例如：'https://kns.cnki.net/KNS8/Navi?DBCode=cjfq&BaseID=KQDX'
    返回 DBCode=cjfq&BaseID=KQDX
    """
    try:
        m0 = re.search(r'Navi\?(.*)', href)
        res = m0.group(1)
    except Exception as e:
        res = '#'
    return res


if __name__ == '__main__':
    sourcehref= 'https://kns.cnki.net/KNS8/Navi?DBCode=cjfq&BaseID=KQDX'
    s = sourceToUrl(sourcehref)
    print(s)
