import re


def author_href_to_url(href,name):
    """ 作者的href转为URL

    目标URL：https://kns.cnki.net/kcms/detail/knetsearch.aspx?dbcode=值1&sfield=au&skey=值2&code=值3

    固定部分：https://kns.cnki.net/kcms/detail/knetsearch.aspx?

    dbcode：获取 href 的 sdb 值
    skey：获取 href 的 skey 值
    code：获取 href 的 acode 值
    """
    baseURL = 'https://kns.cnki.net/kcms/detail/knetsearch.aspx?'
    m1 = re.search(r'sdb=(.*?)&', href)
    m2 = re.search(r'skey=(.*?)&', href)
    m3 = re.search(r'acode=.*', href)
    dbcode = m1.group(0).replace('sdb=', '')
    skey = m2.group(0).replace('skey=', '')
    code = m3.group(0).replace('acode=', '')
    return 'sfield=au&skey={}&code={}'.format(name, code)


def source_href(href):
    """
    爬取到的格式为 https://kns.cnki.net/KNS8/Navi?DBCode=CJFD&BaseID=HXYK ，转化成 DBCode=CJFD&BaseID=HXYK
    """
    m = re.search(r'DBC.*', href)
    return m.group(0)


def stu_href(href):
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


