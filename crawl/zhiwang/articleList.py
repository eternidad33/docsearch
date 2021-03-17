import csv

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class ArticleList:
    """
    爬取知网文章列表页的信息，并存储到CSv文件中
    """

    def __init__(self):
        # 设置浏览器隐藏
        chromeOp = webdriver.ChromeOptions()
        chromeOp.add_argument("headless")
        print("知网爬虫模块启动")
        self.url = "https://www.cnki.net/"
        self.driver = webdriver.Chrome(chrome_options=chromeOp)
        print("正在打开浏览器。。")
        self.driver.get(self.url)
        print("全局等待时间设置为3秒")
        self.driver.implicitly_wait(3)
        print("窗口最大化")
        self.driver.maximize_window()

    def input_keyword(self, keyword):
        print("输入的关键词为{}".format(keyword))
        """
        输入关键词
        :param keyword: 关键词
        """
        key_input = self.driver.find_element_by_id("txt_SearchText")
        key_input.send_keys(keyword)
        key_input.send_keys(Keys.RETURN)

    def crawl(self):
        """
        爬取列表信息,并存储到CSV文件中
        """
        f = open("csv/articlelist.csv", 'a+', encoding='utf-8', newline="")
        f_csv = csv.writer(f)
        # f_csv.writerow(("name", "l", "source", "date", "data"))
        article_table = self.driver.find_element_by_class_name("result-table-list")
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

            # 文献类型
            article_type = article.find_element_by_class_name("data").text

            f_csv.writerow((name, l, source, date, article_type))
            print("【{}】{}----存储完成！".format(name, l))

        print("爬取完成，关闭文件")
        f.close()

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
    a.input_keyword("知识图谱")
    # a.click_relevant()
    # a.click_nextPage()
    a.crawl()
