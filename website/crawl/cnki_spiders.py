import re
import time

import pymysql
import redis
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys

from website.crawl.utils import organizationToUrl, stuToUrl, articleToUrl, extractAuthorCode, sourceToUrl

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "cnki"

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379


class KeyList:
    """关键词列表
    爬取关系，文献发表日期
    关系：文献-来源，文献-作者，存入MySQL关系表中
    发布日期：爬取后存入redis或者直接爬取
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.cnki.net/")
        print("全局等待时间设置为3秒")
        self.driver.implicitly_wait(3)
        print("窗口最大化")
        self.driver.maximize_window()
        self.db = pymysql.connect(host=MYSQL_HOST, user=USERNAME, passwd=PASSWORD, db=DATABASE, port=MYSQL_PORT,
                                  charset='utf8')
        self.curr = self.db.cursor()
        self.r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    def input_keyword(self, keyword):
        """输入关键词"""
        print("输入的关键词为：{}".format(keyword))
        key_input = self.driver.find_element_by_id("txt_SearchText")
        key_input.send_keys(keyword)
        key_input.send_keys(Keys.RETURN)

    def crawl_qikan(self):
        """爬取期刊"""
        # 选择期刊
        try:
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/ul[1]/li[1]/a").click()
        except Exception as e:
            print(e)
            return
        time.sleep(2)
        count = 0
        # 爬取前三页的期刊信息
        for i in range(3):
            # 获取表格行列表
            article_table = self.driver.find_element_by_class_name("result-table-list")
            article_table = article_table.find_element_by_tag_name("tbody")
            article_list = article_table.find_elements_by_tag_name("tr")
            for article in article_list:
                if self._row_qikan(article):
                    count += 1
            next_tag = self.driver.find_element_by_xpath('//*[@id="PageNext"]')
            next_tag.click()
            time.sleep(2)
        print('成功爬取{}文献'.format(count))

    def _row_qikan(self, article):
        """爬取期刊行"""
        # 保存文章标题
        title_tag = article.find_element_by_class_name("name").find_element_by_tag_name("a")
        title = title_tag.text

        # 获取文章url
        url_article = title_tag.get_attribute('href')
        url_article = articleToUrl(url_article)
        if url_article == '#':
            return False

        # 作者url
        author_list_a = article.find_element_by_class_name("author").find_elements_by_tag_name("a")
        authors = []
        for author_a in author_list_a:
            # sfield=au&skey=原雯&code=45345959
            name = author_a.text
            name_url = "sfield=au&skey=" + name + "&code="
            try:
                href = author_a.get_attribute('href')
                code = extractAuthorCode(href)
                name_url = name_url + code
                # 提取code
                authors.append(name_url)
            except NoSuchElementException:
                authors.append('#')

        # 刊名，链接
        source = article.find_element_by_class_name('source').find_element_by_tag_name('a')
        source_name = source.text
        source_href = source.get_attribute('href')
        url_source = sourceToUrl(source_href)

        # 日期
        publish_date = article.find_element_by_class_name('date').text
        # print(title)

        # 存储文献日期到redis
        self.r.set(url_article, publish_date)

        # 文献作者关系存储到mysql表
        for url_author in authors:
            sql_re_aa = "insert into re_article_author(url_article,url_author) values('{}','{}')".format(url_article,
                                                                                                         url_author)
            self._execute_sql(sql_re_aa)

        # 文献来源关系存储到mysql表中
        sql_re_as = "insert into re_article_source(url_article,url_source) values('{}','{}')".format(url_article,
                                                                                                     url_source)
        self._execute_sql(sql_re_as)
        return True

    def _execute_sql(self, sql):
        """执行SQL语句
        :param sql: 要执行的sql语句
        """
        try:
            # 执行sql语句
            self.curr.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print('【成功】{}'.format(sql))
        except Exception as e:
            # 如果发生错误则回滚
            self.db.rollback()
            print('【异常】{}'.format(sql))

    def crawl_lunwen(self):
        """爬取论文"""
        try:
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/ul[1]/li[2]/a").click()
        except Exception as e:
            print(e)
            return
        time.sleep(2)
        for i in range(3):
            # 爬取论文行数据并存入mysql相应关系表
            next_tag = self.driver.find_element_by_xpath('//*[@id="PageNext"]')
            next_tag.click()
            time.sleep(2)

    def crawl(self, keyword):
        """爬取本列表的期刊和论文"""
        self.input_keyword(keyword)
        self.crawl_qikan()
        self.crawl_lunwen()
        # 关闭资源
        self.driver.close()
        self.db.close()
        self.r.close()


class CrawlBase:
    def __init__(self):
        pass

    def crawl(self):
        pass

    def store(self, curr):
        pass


class Article(CrawlBase):
    """文章详情页
    发布日期以键值对形式存到Redis
    直接获取到的信息：标题，摘要，关键词
    作者链接
    """

    def __init__(self, url="FileName=XAJD20210319000&DbName=CAPJLAST&DbCode=CAPJ&"):
        super().__init__()
        self.url = url
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
        req = requests.get("https://kns.cnki.net/kcms/detail/detail.aspx?" + url, headers=headers)
        soup = BeautifulSoup(req.text, 'html5lib')
        # 获取文章主要信息标签
        self.doc = soup.find('div', class_="doc-top")
        self.r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    def crawl(self):
        """爬取文章详情页
        返回字典类型数据，链接url，标题title，摘要summary，关键词keys，作者authors，发布日期date
        """
        # todo 爬取文章详情
        # 获取文章标题
        item = {'title': self.doc.h1.text, 'url': self.url}

        author_list_tag = self.doc.find('h3', id="authorpart")  # 作者列表
        authors = []
        for author_tag in author_list_tag:
            url = ""
            authors.append(url)
            # name = re.sub(r'\d+,\d+', '', author_tag.text)
        item['authors'] = authors

        summary_tag = self.doc.find('span', id='ChDivSummary')
        item['summary'] = summary_tag.text if summary_tag else ''

        # 判断是否有关键词
        flag = self.doc.find('p', class_='keywords')
        key_list = []
        if flag:
            keys_tag = flag.find_all('a')
            for key_tag in keys_tag:
                key_text = re.sub(r'\s|;|；', '', key_tag.text)
                key_list.append(key_text)
            item['keys'] = str(key_list)
        else:
            item['keys'] = ''

        # 从redis中获取发布日期

        self.r.close()
        return item

    def store(self, curr):
        """存储数据
        表：article，re_article_author
        """
        item = self.crawl()


class Author(CrawlBase):
    """作者详情页
    信息：主修专业，总发文量，总下载量
    关系：作者-文献，师生，所在机构，同机构的合作者
    """
    # todo 爬取作者详情页
    def __init__(self, url="dbcode=CAPJ&sfield=au&skey=%e6%9d%a8%e7%92%90&code=36280603"):
        super().__init__()
        self.url = url
        new_url = 'https://kns.cnki.net/kcms/detail/knetsearch.aspx?' + url
        chromeOp = webdriver.ChromeOptions()
        chromeOp.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=chromeOp)
        self.driver.get(new_url)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def crawl(self):
        """爬取作者详情
        返回字典：链接url，姓名name，主修专业major，总发布量sum_publish，总下载量sum_download，
        文献articles，老师teachers，学生students，所在机构organization，同机构的合作者cooperations
        """
        item = {'url': self.url}
        name_tag = self.driver.find_element_by_tag_name("h1")
        organization = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[3]/h3[1]/span/a')
        major_tag = self.driver.find_element_by_xpath("//div/h3[2]")
        sum_public_tag = self.driver.find_element_by_xpath('//h5/em[1]')
        sum_download_tag = self.driver.find_element_by_xpath('//h5/em[2]')
        item['name'] = name_tag.text if name_tag else ""
        item['major'] = major_tag.text if major_tag else ""
        item['sum_publish'] = sum_public_tag.text if sum_public_tag else ""
        item['sum_download'] = sum_download_tag.text if sum_download_tag else ""
        s = organization.get_attribute('onclick') if organization else ""
        item['organization'] = organizationToUrl(s) if s else ""
        item['teachers'] = self._crawl_teachers()
        item['students'] = self._crawl_students()
        item['articles'] = self._crawl_articles()
        item['cooperation'] = self._crawl_cooperation()
        return item

    def _crawl_articles(self):
        """爬取作者的文献"""
        res = []
        try:
            # 跳回原框架
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frame2")
        except NoSuchElementException:
            print("作者无文献！")
        except WebDriverException:
            print("进入框架frame2异常！")
        return res

    def _crawl_teachers(self):
        """爬取作者的导师"""
        res = []
        try:
            # 跳回原框架
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frame9")
            name_tag = self.driver.find_element_by_class_name('name')
            a_tag = name_tag.find_element_by_tag_name('a')
            s = a_tag.get_attribute('onclick')
            s = re.sub(r'\s', '', s)
            m = re.search(r'\((.*?)\)', s)
            temp = m.group(0)
            t = stuToUrl(temp)
            res.append(t)
            # self.teacher = name_tag.text
            # print("【作者导师】{0: <12} 爬取成功！".format(self.teacher))
        except NoSuchElementException:
            print("作者无导师！")
        except WebDriverException:
            print("进入框架frame9异常！")
        return res

    def _crawl_students(self):
        """爬取作者学生，返回学生链接列表"""
        res = []
        try:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frame12")
            listcon_tag = self.driver.find_element_by_class_name('listcont')
            lis = listcon_tag.find_elements_by_tag_name('li')
            for li in lis:
                a_tag = li.find_element_by_tag_name('a')
                s = a_tag.get_attribute('onclick')
                s = re.sub(r'\s', '', s)
                m = re.search(r'\((.*?)\)', s)
                temp = m.group(0)
                t = stuToUrl(temp)
                res.append(t)
        except NoSuchElementException:
            print("作者无学生！")
        except WebDriverException:
            print("进入框架frame12异常！")
        return res

    def _crawl_cooperation(self):
        res = []
        try:
            # 跳回原框架
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frame10")
        except NoSuchElementException:
            print("作者无同机构合作者！")
        except WebDriverException:
            print("进入框架frame10异常！")
        return res

    def store(self, curr):
        """存储数据
        表：author，re_article_author，re_author_organization，re_teacher_student
        """
        pass


class Source(CrawlBase):
    """文献来源
    信息：名称，基本信息，出版信息，评估信息
    关系：文献链接
    """
    # todo 爬取文献来源详情
    def __init__(self, url):
        super().__init__()

    def crawl(self):
        pass

    def store(self, curr):
        pass


class Organization(CrawlBase):
    """作者机构
    直接获取的信息：名称，曾用名，地域，官网
    机构主要作者,主办刊物
    """
    # todo 爬取作者机构详情
    def __init__(self, url):
        super().__init__()

    def crawl(self):
        pass

    def store(self, curr):
        pass


def getArticleUrls():
    """获取未被爬取的文献链接"""
    pass


def getAuthorsUrls():
    """获取未被爬取的作者链接"""
    pass


def getSourceUrls():
    """获取未被爬取的文献来源链接"""
    pass


def getOrganizationUrls():
    """获取未被爬取的文献来源链接"""
    pass


def crawlArticle(urls):
    """爬取未被爬取的文章"""
    pass


def crawlAuthor(urls):
    """爬取未被爬取的作者"""
    pass


def crawlSource(urls):
    """爬取未被爬取的文献来源"""
    pass


def crawlOrganization(urls):
    """爬取未被爬取的学者所在单位"""
    pass
