from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


def loadDriver():
    """加载驱动，打开知网
    :return:
    """
    driver = webdriver.Firefox()
    driver.get('https://www.cnki.net/')
    return driver


def inputKeyword(driver, key):
    """输入关键词
    :param driver:
    :param key:
    :return:
    """
    key_word = key
    key_input = driver.find_element_by_id("txt_SearchText")
    key_input.send_keys(key_word)
    key_input.send_keys(Keys.RETURN)


def getArticle(driver):
    """获取文章的标题，作者，来源，发表时间，数据库
    :param driver:
    :return:
    """
    article_table = driver.find_element_by_class_name("result-table-list")
    article_table = article_table.find_element_by_tag_name("tbody")
    article_list = article_table.find_elements_by_tag_name("tr")
    for article in article_list:
        # 保存文章标题
        name = article.find_element_by_class_name("name").find_element_by_tag_name("a").text

        # 保存作者列表
        l = []
        author_list = article.find_element_by_class_name("author").find_elements_by_tag_name("a")
        if len(author_list) == 0:
            l.append(article.find_element_by_class_name("author").text)
        for author in author_list:
            l.append(author.text)

        # 保存来源
        source = article.find_element_by_class_name("source").text

        # 发表时间
        date = article.find_element_by_class_name("date").text

        # 数据库
        data = article.find_element_by_class_name("data").text

        print(name, l, source, date, data, )
