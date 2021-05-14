import random
import time

import pymysql
import redis
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys

from website.crawl.utils import *

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "cnkidemo"

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

    def crawl_lunwen(self):
        """爬取论文"""
        try:
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/ul[1]/li[2]/a").click()
        except Exception as e:
            print(e)
            return
        time.sleep(2)
        count = 0
        for i in range(3):
            # 获取表格行列表
            article_table = self.driver.find_element_by_class_name("result-table-list")
            article_table = article_table.find_element_by_tag_name("tbody")
            article_list = article_table.find_elements_by_tag_name("tr")
            for article in article_list:
                if self._row_lunwen(article):
                    count += 1
            # 爬取论文行数据并存入mysql相应关系表
            next_tag = self.driver.find_element_by_xpath('//*[@id="PageNext"]')
            next_tag.click()
            time.sleep(2)
        print('成功爬取{}论文'.format(count))

    def crawl(self, keyword):
        """爬取本列表的期刊和论文"""
        self.input_keyword(keyword)
        self.crawl_qikan()
        self.crawl_lunwen()
        # 关闭资源
        self.driver.close()
        self.db.close()
        self.r.close()

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

        # # 作者url
        # author_list_a = article.find_element_by_class_name("author").find_elements_by_tag_name("a")
        # authors = []
        # for author_a in author_list_a:
        #     # sfield=au&skey=原雯&code=45345959
        #     name = author_a.text
        #     name_url = "sfield=au&skey=" + name + "&code="
        #     try:
        #         href = author_a.get_attribute('href')
        #         code = extractAuthorCode(href)
        #         name_url = name_url + code
        #         # 提取code
        #         authors.append(name_url)
        #     except NoSuchElementException:
        #         authors.append('#')

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

        # # 文献作者关系存储到mysql表
        # for url_author in authors:
        #     sql_re_aa = "insert into re_article_author(url_article,url_author) " \
        #                 "values('{}','{}')".format(url_article, url_author)
        #     self._execute_sql(sql_re_aa)

        # 文献来源关系存储到mysql表中
        sql_re_as = "insert into re_article_source(url_article,url_source) " \
                    "values('{}','{}')".format(url_article, url_source)
        self._execute_sql(sql_re_as)
        return True

    def _row_lunwen(self, article):
        """爬取期刊行"""
        # 保存文章标题
        title_tag = article.find_element_by_class_name("name").find_element_by_tag_name("a")
        title = title_tag.text

        # 获取论文url
        url_article = title_tag.get_attribute('href')
        url_article = lunwenToUrl(url_article)
        if url_article == '#':
            return False

        # 获取学校来源url
        unit = article.find_element_by_class_name('unit').find_element_by_tag_name('a')
        school_name = unit.text
        source_href = unit.get_attribute('href')
        url_school = sourceToUrl(source_href)

        # 文献来源关系存储到mysql表中
        sql_re_as = "insert into re_article_source(url_article,url_source) " \
                    "values('{}','{}')".format(url_article, url_school)
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


class CrawlBase:
    def __init__(self):
        pass

    def crawl(self):
        pass

    def store(self, db):
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
        # headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
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
        # 获取文章标题
        item = {'title': self.doc.h1.text, 'url': self.url}

        author_list_tag = self.doc.find('h3', id="authorpart")  # 作者列表
        authors = []
        if not author_list_tag:
            pass
        else:
            for author_tag in author_list_tag:
                try:
                    # 作者可能没有href
                    href = author_tag.a.get('onclick')
                    # name = re.sub(r'\d+,\d+', '', author_tag.text)
                    url = auToUrl(href)
                    authors.append(url)
                except:
                    continue
        if 'CMFD' in self.url or 'CDFD' in self.url:
            # 论文的作者只有一个
            try:
                a_tag = self.doc.find('a', class_='author')
                href = a_tag.get('onclick')
                url = auToUrl(href)
                authors.append(url)
            except:
                # 作者无链接
                pass
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
        item['date'] = self.r.get(self.url)
        self.r.close()
        return item

    def store(self, db):
        """存储数据表：article，re_article_author"""
        item = self.crawl()
        url = item['url']
        title = item['title']
        summary = item['summary']
        keywords = re.sub(r"\[|\]|'", '', item['keys'])
        date = item['date'] if item['date'] else '2020-01-01'
        sql_a = "insert into article(url, title, summary, keywords, date) " \
                "VALUES ('{}','{}','{}','{}','{}')".format(url, title, summary, keywords, date)
        executeSql(db, sql_a)
        for au in item['authors']:
            sql_re_aa = "insert into re_article_author(url_article, url_author) " \
                        "VALUES ('{}','{}')".format(url, au)
            executeSql(db, sql_re_aa)


class Author(CrawlBase):
    """作者详情页
    信息：主修专业，总发文量，总下载量
    关系：作者-文献，师生，所在机构，同机构的合作者
    """

    def __init__(self, url="skey=王宁&code=33167488"):
        super().__init__()
        self.url = url
        new_url = 'https://kns.cnki.net/kcms/detail/knetsearch.aspx?sfield=au&' + url
        # fireOp = webdriver.FirefoxOptions()
        # fireOp.add_argument("headless")
        # self.driver = webdriver.Firefox(firefox_options=fireOp)
        # chromeOp = webdriver.ChromeOptions()
        # chromeOp.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=chromeOp)
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get(new_url)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

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

    def store(self, db):
        """存储数据
        表：author，re_article_author，re_author_organization，re_teacher_student
        """
        try:
            item = self.crawl()
        except NoSuchElementException:
            url = self.url
            m = re.search('skey=(.*?)&', url)
            name = m.group(1) if m else "##########"
            sql0 = "insert into author(url,name) values('{}','{}')".format(self.url, name)
            executeSql(db, sql0)
            print('无法获取作者相关信息')
            return
        url = item['url']
        name = item['name']
        major = item['major']
        organization = item['organization']
        sum_publish = item['sum_publish']
        sum_download = item['sum_download']
        # 插入作者
        sql_a = "INSERT INTO author(url,name,major,sum_publish,sum_download) " \
                "VALUES ('{}','{}','{}','{}','{}')".format(url, name, major, sum_publish, sum_download)
        executeSql(db, sql_a)

        # 插入作者组织关系
        sql_ao = "INSERT INTO re_author_organization(url_author, url_organization) " \
                 "VALUES ('{}','{}')".format(url, organization)
        executeSql(db, sql_ao)

        # 插入文章作者关系
        articles = item['articles']
        for article in articles:
            sql_aa = "INSERT INTO re_article_author(url_article, url_author) " \
                     "VALUES ('{}','{}')".format(article, url)
            executeSql(db, sql_aa)

        # 插入师生关系
        teachers = item['teachers']
        students = item['students']
        for teacher in teachers:
            sql_ts = "INSERT INTO re_teacher_student(url_teacher, url_student) " \
                     "VALUES ('{}','{}')".format(teacher, url)
            executeSql(db, sql_ts)

        for student in students:
            sql_st = "INSERT INTO re_teacher_student(url_teacher, url_student) " \
                     "VALUES ('{}','{}')".format(url, student)
            executeSql(db, sql_st)

        # 同机构合作者的插入作者组织关系
        coop = item['cooperation']
        for co in coop:
            sql_co = "INSERT INTO re_author_organization(url_author,url_organization) " \
                     "VALUES ('{}','{}')".format(co, organization)
            executeSql(db, sql_co)

    def _crawl_articles(self):
        """爬取他发表的文献
        frame3为他发表的期刊文献，frame7为论文"""
        res = []
        # todo 爬取作者详情页的期刊
        # try:
        #     # 跳回原框架
        #     self.driver.switch_to.default_content()
        #     self.driver.switch_to.frame("frame3")
        #     ul_tag=self.driver.find_element_by_class_name('bignum')
        #     lis=ul_tag.find_elements_by_tag_name('li')
        #     for li in lis:
        #         # 抽取期刊文献信息
        #         pass
        # except NoSuchElementException:
        #     print("作者无期刊文献！")
        # except WebDriverException:
        #     print("进入框架frame3异常！")
        try:
            # 跳回原框架
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frame7")
            ul_tag = self.driver.find_element_by_class_name('bignum')
            lis = ul_tag.find_elements_by_tag_name('li')
            for li in lis:
                text = li.text
                # print(text)
                m = re.search(r'\d{4}', text)
                year = m.group(0)
                tag_a = li.find_element_by_tag_name('a')
                href = tag_a.get_attribute('href')
                url = articleToUrl(href)
                # print(tag_a.text + ',发表年份：' + year)
                date = year + '-01-01'
                self.r.set(url, date)
                # print(url)
                res.append(url)
        except NoSuchElementException:
            print("作者无博硕论文文献！")
        except WebDriverException:
            print("进入框架frame7异常！")
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
            h3 = self.driver.find_element_by_tag_name('h3')
            # print(h3.text)
            if '同机构' not in h3.text:
                raise NoSuchElementException
            ul = self.driver.find_element_by_class_name('col8')
            lis = ul.find_elements_by_tag_name('li')
            for li in lis:
                a_tag = li.find_element_by_tag_name('a')
                href = a_tag.get_attribute('onclick')
                s = re.sub(r'\s', '', href)
                m = re.search(r'\((.*?)\)', s)
                temp = m.group(0)
                t = stuToUrl(temp)
                res.append(t)
        except NoSuchElementException:
            print("作者无同机构合作者！")
        except WebDriverException:
            print("进入框架frame10异常！")
        return res

    def close(self):
        self.driver.close()
        self.r.close()


class Source(CrawlBase):
    """文献来源
    信息：名称，基本信息，出版信息，评估信息
    关系：文献链接
    """

    def __init__(self, url):
        super().__init__()
        self.url = url
        newurl = 'https://kns.cnki.net/KNS8/Navi?' + url
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
        req = requests.get(newurl, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        # 通过分析页面信息，要爬取的信息都存在dl标签中
        self.dl = soup.dl

    def crawl(self):
        item = {'url': self.url}
        if not self.dl:
            print('【dl标签异常】无法获取dl标签')
            return
        name_tag = self.dl.h3
        name = name_tag.text if name_tag else ''

        name_en_tag = name_tag.p
        name_en = name_en_tag.text if name_en_tag else ''
        temp = re.sub(r'\s', '', name_en) if name_en else ''
        item['name'] = re.sub(r'\s*|{}'.format(temp), '', name)
        item['name'] = item['name'].replace(temp, '')
        item['name'] = re.sub(r'\d*', '', item['name'])
        item['en-name'] = name_en
        uls = self.dl.findAll('ul')
        if len(uls) == 2:
            # 基本信息,出版概况
            basic = uls[0].text
            publish = uls[1].text
            basic = re.sub(r'基本信息|\s*', '', basic)
            publish = re.sub(r'出版概况|\s', '', publish)
            item['basic'] = basic
            item['publish'] = publish
            item['evaluation'] = ''
        elif len(uls) == 3:
            # 基本信息，出版信息，评价信息
            basic = uls[0].text
            publish = uls[1].text
            evaluation = uls[2].text
            basic = re.sub(r'基本信息|\s*', '', basic)
            publish = re.sub(r'出版信息|\s*', '', publish)
            evaluation = re.sub(r'评价信息|\s*', '', evaluation)
            item['basic'] = basic
            item['publish'] = publish
            item['evaluation'] = evaluation
        else:
            item['basic'] = ''
            item['publish'] = ''
            item['evaluation'] = ''

        return item

    def store(self, db):
        item = self.crawl()
        if not item:
            return
        url = item['url']
        name = item['name']
        basic = item['basic']
        publish = item['publish']
        evaluation = item['evaluation']
        sql = "insert into source(url, name, basic_info, publish_info, evaluation) " \
              "VALUES ('{}','{}','{}','{}','{}')".format(url, name, basic, publish, evaluation)
        executeSql(db, sql)


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

    def store(self, db):
        pass


def executeSql(db, sql):
    """执行sql语句"""
    try:
        curr = db.cursor()
        # 执行sql语句
        curr.execute(sql)
        # 提交到数据库执行
        db.commit()
        print('【成功】{}'.format(sql))
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()
        print('【异常】{}'.format(sql))


def getArticleUrls(db):
    """获取未被爬取的文献链接"""
    # sql1 = "SELECT DISTINCT article.url FROM article LEFT JOIN re_article_author ON article.url=re_article_author.url_article WHERE re_article_author.url_article is NULL"
    sql = 'SELECT DISTINCT re_article_source.url_article ' \
          'FROM re_article_source ' \
          'LEFT JOIN article ON re_article_source.url_article=article.url ' \
          'WHERE article.url is NULL'
    curr = db.cursor()
    curr.execute(sql)
    urls = []
    for data in curr.fetchall():
        url = data[0]
        urls.append(url)
    return urls


def crawlArticle(urls, db):
    """爬取未被爬取的文章"""
    print("需要爬取的文献个数为 {}".format(len(urls)))
    for url in urls:
        time.sleep(2)
        article = Article(url)
        # item = a.crawl()
        article.store(db)
        # print(item)


def getAuthorsUrls(db):
    """获取未被爬取的作者链接"""
    sql_aa = 'SELECT DISTINCT re_article_author.url_author ' \
             'FROM re_article_author ' \
             'LEFT JOIN author ON re_article_author.url_author=author.url ' \
             'WHERE author.url is NULL'
    sql_ao = """
                SELECT DISTINCT
                    re_author_organization.url_author
                FROM
                    re_author_organization
                LEFT JOIN author ON re_author_organization.url_author = author.url
                WHERE
                    author.url IS NULL
                """
    curr = db.cursor()
    curr.execute(sql_aa)
    urls = []
    for data in curr.fetchall():
        url = data[0]
        urls.append(url)
    # curr.execute(sql_ao)
    # for data in curr.fetchall():
    #     url = data[0]
    #     urls.append(url)
    return urls


def crawlAuthor(urls, db):
    """爬取未被爬取的作者"""

    length = len(urls)
    count = 0
    for url in urls:
        rand = random.randint(1, 5)
        time.sleep(rand)
        author = Author(url)
        author.store(db)
        author.close()
        count += 1
        print('以爬取完成：{}/{}'.format(count, length))


def getSourceUrls(db):
    """获取未被爬取的文献来源链接"""
    sql = """
            SELECT DISTINCT
                re_article_source.url_source
            FROM
                re_article_source
            LEFT JOIN source ON re_article_source.url_source = source.url
            WHERE
                source.url IS NULL
	        """
    # sql = 'SELECT DISTINCT re_article_source.url_source FROM re_article_source LEFT JOIN source ON re_article_source.url_article=source.url WHERE source.url is NULL'
    curr = db.cursor()
    curr.execute(sql)
    urls = []
    for data in curr.fetchall():
        url = data[0]
        urls.append(url)
    return urls


def crawlSource(urls, db):
    """爬取未被爬取的文献来源"""
    print("需要爬取的文献来源个数为 {}".format(len(urls)))
    for url in urls:
        time.sleep(2)
        source = Source(url)
        source.store(db)


def getOrganizationUrls():
    """获取未被爬取的作者所在机构链接"""
    pass


def crawlOrganization(urls):
    """爬取未被爬取的学者所在单位"""
    pass
