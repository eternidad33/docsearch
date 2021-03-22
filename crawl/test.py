import re


def author_href_to_url(href):
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
    return '{}dbcode={}sfield=au&skey={}code={}'.format(baseURL, dbcode, skey, code)
