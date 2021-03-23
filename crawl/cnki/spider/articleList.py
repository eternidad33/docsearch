import re

import pymysql
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from myUtils.urlUtil import author_href_to_url


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
                # print(i, source, url_source)
            except:
                continue

            # 文献类型
            article_type = article.find_element_by_class_name("data").text

            # 保存文章标题
            name_tag = article.find_element_by_class_name("name").find_element_by_tag_name("a")
            name = name_tag.text

            # 获取文章url
            url_article = name_tag.get_attribute('href')
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

            # 保存作者列表
            author_list = []
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
                    try:
                        # 执行sql语句
                        self.curr.execute(insert_aa)
                        # 提交到数据库执行
                        self.db.commit()
                        print('【成功】文献作者\t{}---{} 插入mysql'.format(name, author_name))
                    except:
                        # 如果发生错误则回滚
                        self.db.rollback()
                        print('【异常】文献作者\t{}---{} 插入异常'.format(name, author_name))

                d = {'name': author_name, 'href': author_href}
                author_list.append(d)

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
                    try:
                        # 执行sql语句
                        self.curr.execute(insert_aa)
                        # 提交到数据库执行
                        self.db.commit()
                        print('【成功】文献作者\t{}---{}插入mysql'.format(name, author_name))
                    except:
                        # 如果发生错误则回滚
                        self.db.rollback()
                        print('【异常】文献作者\t{}---{}插入异常'.format(name, author_name))
                d = {'name': author_name, 'href': author_href}
                author_list.append(d)

            # 发表时间
            date = article.find_element_by_class_name("date").text
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


if __name__ == '__main__':
    a = ArticleList()
    a.input_keyword("人工智能")
    a.crawl()
