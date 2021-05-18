import re


def organizationToUrl(href):
    """将作者机构字符串转换为相应链接
    例如："\n                        TurnPageToKnet('in','南京邮电大学','0101257')\n
    转换成 “sfield=in&skey=南京邮电大学&code=0101257”
    """
    res = '#'
    start, end = href.index('(') + 1, href.index(')')
    s = href[start:end]
    list0 = s.replace("'", "").split(',')
    if len(list0) > 2:
        res = "sfield=" + list0[0] + "&skey=" + list0[1] + "&code=" + list0[2]
    return res


def stuToUrl(href):
    """
    将('au','王永超','42141239')
    转换成 skey=王永超&code=42141239
    访问链接：https://kns.cnki.net/kcms/detail/knetsearch.aspx?+返回值
    """
    ss = href.split(',')
    m1 = re.search(r"'(.*?)'", ss[0])
    m2 = re.search(r"'(.*?)'", ss[1])
    m3 = re.search(r"'(.*?)'", ss[2])
    sfield = m1.group(0).replace("'", "")
    skey = m2.group(0).replace("'", "")
    code = m3.group(0).replace("'", "")

    # return 'sfield={}&skey={}&code={}'.format(sfield, skey, code)
    return 'skey={}&code={}'.format(skey, code)


def articleToUrl(href):
    """将关键词列表的期刊文章url转换成相应的字符串
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


def lunwenToUrl(href):
    """将关键词列表的论文url转换成相应的字符串
    例如：'https://kns.cnki.net/KNS8/Detail?sfield=fn&QueryID=5&CurRec=1&DbCode=CDFD&dbname=CDFDLAST2021&filename=1021021170.nh'
    返回：'dbcode=CDFD&dbname=CDFDLAST2021&filename=1021021170.NH'
    """
    res = '#'
    try:
        href = href.upper()
        m0 = re.search(r"DBCODE=(.*?)&", href)
        m1 = re.search(r'DBNAME=(.*?)&', href)
        m2 = re.search(r'FILENAME=(.*)', href)
        dbcode = m0.group(1)
        dbname = m1.group(1)
        filename = m2.group(1)
        res = 'dbcode=' + dbcode + '&dbname=' + dbname + '&filename=' + filename
    except Exception as e:
        res = '#'
    return res


def auToUrl(href: str):
    """提取skey和code
    参数形式："\n                                  TurnPageToKnetV('au','王宁','33167488','-1jneb6HWg72-buRfraVc4ne9yN6-0WXaAnsWNgRfSH807I0dZ5EdylOABmJ53Mf');\n                                "
    :return: str skey=王宁&code=33167488
    """
    try:
        href = re.sub(r'\s', '', href)
        start, end = href.index('(') + 1, href.index(')')
        href = href[start:end]
        # 'au','王宁','33167488','-1jneb6HWg72-buRfraVc4ne9yN6-0WXaAnsWNgRfSH807I0dZ5EdylOABmJ53Mf'
        # 去掉',以，划分
        href = href.replace("'", '')
        ls = href.split(',')
        if len(ls) > 2:
            skey = ls[1]
            code = ls[2]
            return 'skey=' + skey + '&code=' + code
    except Exception as e:
        return '#'


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


def extractAuthorName(href):
    """抽取作者姓名
    例如：skey=李鑫&code=04558829
    返回：李鑫
    """
    pattern = 'skey=(.*?)&'
    m = re.search(pattern, href)
    try:
        res = m.group(1)
    except:
        res = ''
    return res


def extractArticleFileName(href):
    """抽取文章filename
    例如：dbcode=CMFD&dbname=CMFDTEMP&filename=1021023887.NH
    返回：1021023887.NH
    """
    pattern = 'filename=(.*)'
    m = re.search(pattern, href)
    try:
        res = m.group(1)
    except:
        res = ''
    return res


def extractBaseID(href):
    """抽取sourceURL的baseID
    例如：DBCode=CDMD&BaseID=GBFGU
    返回：GBFGU
    """
    pattern = 'BaseID=(.*)'
    m = re.search(pattern, href)
    try:
        res = m.group(1)
    except:
        res = ''
    return res


def extractOrganizationName(href):
    """抽取organization的name
    例如：sfield=in&skey=上海建工集团&code=0208315
    返回：上海建工集团
    """
    pattern = 'skey=(.*?)&'
    m = re.search(pattern, href)
    try:
        res = m.group(1)
    except:
        res = ''
    return res


if __name__ == '__main__':
    sourcehref = 'https://kns.cnki.net/KNS8/Navi?DBCode=cjfq&BaseID=KQDX'
    lunwen_url = 'https://kns.cnki.net/KNS8/Detail?sfield=fn&QueryID=5&CurRec=1&DbCode=CDFD&dbname=CDFDLAST2021&filename=1021021170.nh'
    au = "\n                                  TurnPageToKnetV('au','王宁','33167488','-1jneb6HWg72-buRfraVc4ne9yN6-0WXaAnsWNgRfSH807I0dZ5EdylOABmJ53Mf');\n                                "
    a = auToUrl(au)
    print(a)
    au = 'skey=李鑫&code=04558829'
    at = 'dbcode=CMFD&dbname=CMFDTEMP&filename=1021023887.NH'
    print(extractArticleFileName(at))
