from py2neo import Graph


def search_key(graph, key):
    cql = "Match (n:Article) where n.title=~'.*{}.*' " \
          "return n.title as title,n.summary as summary".format(key)
    try:
        currsor = graph.run(cql)
        return currsor.to_data_frame()
    except Exception as e:
        return "【异常】图数据未收集相关数据".format(e)


if __name__ == '__main__':
    g = Graph(auth=('neo4j', '123456'))
    pd = search_key(g, '知识图谱')
