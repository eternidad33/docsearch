import re

import pymysql
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from myUtils.urlUtil import author_href_to_url, source_href


class ArticleList:
    """
    爬取知网文章列表页的信息，并存储到CSv文件中
    """

    def __init__(self):
        self.url = "https://www.cnki.net/"
        print("知网爬虫模块启动")
        self.db = pymysql.connect(host='localhost', user='root', passwd='123456', db='cnki', port=3306, charset='utf8')
        self.curr = self.db.cursor()
        # 设置浏览器隐藏
        chromeOp = webdriver.ChromeOptions()
        chromeOp.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=chromeOp)
        # self.driver = webdriver.Chrome()

        print("正在打开浏览器。。")
        self.driver.get(self.url)

        print("全局等待时间设置为3秒")
        self.driver.implicitly_wait(3)

        print("窗口最大化")
        self.driver.maximize_window()

    def input_keyword(self, keyword):
        """
        输入关键词
        :param keyword: 关键词
        """
        print("输入的关键词为{}".format(keyword))
        key_input = self.driver.find_element_by_id("txt_SearchText")
        key_input.send_keys(keyword)
        key_input.send_keys(Keys.RETURN)

    def crawl(self):
        """
        爬取列表信息
        """

        # 获取文章列表行
        article_table = self.driver.find_element_by_class_name("result-table-list")
        article_table = article_table.find_element_by_tag_name("tbody")
        article_list = article_table.find_elements_by_tag_name("tr")
        i = 1
        for article in article_list:
            # 保存来源
            source_tag = article.find_element_by_class_name("source")
            source = source_tag.text
            try:
                a_tag = source_tag.find_element_by_tag_name('a')
                url_source = a_tag.get_attribute('href') if a_tag else ''
                url_source = source_href(url_source)
                # print(i, source, url_source)
            except:
                continue

            # 文献类型
            article_type = article.find_element_by_class_name("data").text

            # 保存文章标题
            title_tag = article.find_element_by_class_name("name").find_element_by_tag_name("a")
            title = title_tag.text

            # 获取文章url
            url_article = title_tag.get_attribute('href')
            match = re.search(r'FileName=(.*?)&DbName=(.*?)&DbCode=(.*?)&', url_article)
            if match:
                url_article = match.group(0)
            elif article_type.find('外文') != -1:
                """判断是否为外文期刊"""
                print('发现外文期刊')
                continue
            else:
                url_article = '#'
                continue

            insert_as = "insert into re_article_source(url_article,url_source) values ('{}','{}')".format(
                url_article, url_source)
            self.execute_sql(insert_as, '文献来源\t{}'.format(title))

            author_list_a = article.find_element_by_class_name("author").find_elements_by_tag_name("a")
            # 只有一个作者，作者可能无链接
            if len(author_list_a) == 0:
                author_name = article.find_element_by_class_name("author").text
                try:
                    author_href = article.find_element_by_class_name('author').find_element_by_tag_name(
                        'a').get_attribute('href')
                except NoSuchElementException:
                    author_href = '#'
                if author_href != '#' and author_name:
                    author_href = author_href_to_url(author_href)
                    # print(author_name, author_href)
                    insert_aa = "insert into re_article_author(url_article,url_author) values ('{}','{}')".format(
                        url_article, author_href)
                    self.execute_sql(insert_aa, '{}---{}'.format(title, author_name))

            # 包含多个作者
            for author_a in author_list_a:
                author_name = author_a.text
                try:
                    author_href = author_a.get_attribute('href')
                except NoSuchElementException:
                    author_href = '#'
                if author_href != '#' and author_name:
                    author_href = author_href_to_url(author_href)
                    # print(author_name, author_href)
                    insert_aa = "insert into re_article_author(url_article,url_author) values ('{}','{}')".format(
                        url_article, author_href)
                    self.execute_sql(insert_aa, '文献作者\t{}---{}'.format(title, author_name))

            # 发表时间
            date = article.find_element_by_class_name("date").text
            insert_a = "insert into article_ex(url,publish_date,type) values ('{}','{}','{}')".format(
                url_article, date, article_type)
            self.execute_sql(insert_a, '日期类型\t{}'.format(title))

            i += 1

        print("爬取完成，关闭数据库，关闭驱动")
        self.db.close()
        self.driver.close()

    def click_relevant(self):
        """
        点击相关度
        """
        relevant = self.driver.find_element_by_xpath("//*[@id='orderList']/li[1]")
        ActionChains(self.driver).click(relevant).perform()

    def click_nextPage(self):
        """
        点击下一页
        """
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # nextPage = self.driver.find_element_by_xpath('//*[@id="PageNext"]')
        # ActionChains(self.driver).click(nextPage).perform()
        ActionChains(self.driver).send_keys(Keys.RIGHT).perform()

    def execute_sql(self, sql, message=''):
        """
        执行SQL语句
        :param sql: 要执行的sql语句
        :param message: 提示消息
        """
        try:
            # 执行sql语句
            self.curr.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print('【成功】{}'.format(message))
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            print('【异常】{}'.format(message))


if __name__ == '__main__':
    a = ArticleList()
    a.input_keyword("人工智能")
    a.crawl()
