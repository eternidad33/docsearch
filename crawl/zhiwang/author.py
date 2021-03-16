import csv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException


class Author:
    name = ''
    school = ''
    major = ''
    sum_public = ''
    sum_download = ''
    fields = []
    articles = []
    teacher = ''
    students = []

    def __init__(self,
                 url="https://kns.cnki.net/kcms/detail/knetsearch.aspx?dbcode=CMFD&sfield=au&skey=%e8%82%96%e7%9b%b8%e6" \
                     "%ac%a3&code=42962547&v=XuuQ%25mmd2Fi3qrWQVFULCjpwXoY%25mmd2BbZqrZ3W7KIDLXBs226SGLHyEOO6LJv4PgXwW" \
                     "%25mmd2BwxsG "):
        print("开始爬取作者信息")
        self.driver = webdriver.Chrome()
        print("正在打开浏览器。。")
        self.driver.get(url)
        print("全局等待时间设置为3秒")
        self.driver.implicitly_wait(3)
        print("窗口最大化")
        self.driver.maximize_window()

    def crawl_main(self):
        """
        爬取主要信息：姓名，学校，专业，总发文量，总下载量
        """
        name_tag = self.driver.find_element_by_tag_name("h1")
        school_tag = self.driver.find_element_by_xpath("//div/h3[1]")
        major_tag = self.driver.find_element_by_xpath("//div/h3[2]")
        sum_public_tag = self.driver.find_element_by_xpath('//h5/em[1]')
        sum_download_tag = self.driver.find_element_by_xpath('//h5/em[2]')
        self.name = name_tag.text if name_tag else ""
        self.school = school_tag.text if school_tag else ""
        self.major = major_tag.text if major_tag else ""
        self.sum_public = sum_public_tag.text if sum_public_tag else ""
        self.sum_download = sum_download_tag.text if sum_download_tag else ""
        print("【作者信息】{0: ^12} 爬取成功！".format(self.name))

    def crawl_fields(self):
        """爬取作者关注领域"""
        try:
            # 跳回原框架
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frame1")
            listcon_tag = self.driver.find_element_by_class_name('listcont')
            lis = listcon_tag.find_elements_by_tag_name('li')
            for li in lis:
                self.fields.append(li.text)
                print("【关注领域】{0: <12} 爬取成功！".format(li.text))
        except NoSuchElementException:
            print("作者无关注领域！")
        except WebDriverException:
            print("进入框架frame1异常！")

    def crawl_articles(self):
        """爬取作者的文献"""
        try:
            # 跳回原框架
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frame2")
            ul_tag = self.driver.find_element_by_xpath("//div/ul")
            lis = ul_tag.find_elements_by_tag_name('li')
            for li in lis:
                temp = li.find_element_by_tag_name('a').text
                self.articles.append(temp)
                print("【作者文献】{0: <20} 爬取成功！".format(temp))
        except NoSuchElementException:
            print("作者无文献！")
        except WebDriverException:
            print("进入框架frame2异常！")

    def crawl_teacher(self):
        """爬取作者导师"""
        try:
            # 跳回原框架
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frame9")
            name_tag = self.driver.find_element_by_class_name('name')
            self.teacher = name_tag.text
            print("【作者导师】{0: <12} 爬取成功！".format(self.teacher))
        except NoSuchElementException:
            print("作者无导师！")
        except WebDriverException:
            print("进入框架frame9异常！")

    def crawl_students(self):
        """爬取作者学生"""
        try:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frame12")
            listcon_tag = self.driver.find_element_by_class_name('listcont')
            lis = listcon_tag.find_elements_by_tag_name('li')
            for li in lis:
                self.students.append(li.text)
                print("【作者学生】{0: <12} 爬取成功！".format(li.text))
        except NoSuchElementException:
            print("作者无学生！")
        except WebDriverException:
            print("进入框架frame12异常！")

    def close_driver(self):
        """关闭当前页面"""
        self.driver.close()

    def save_csv(self, f):
        """存储到csv文件中"""
        self.crawl_main()
        self.crawl_fields()
        self.crawl_articles()
        self.crawl_teacher()
        self.crawl_students()
        f_csv = csv.writer(f)
        f_csv.writerow((self.name, self.school, self.major, self.sum_public, self.sum_download, self.fields,
                        self.articles, self.teacher, self.students))
        self.close_driver()


if __name__ == '__main__':
    # url = "https://kns.cnki.net/kcms/detail/knetsearch.aspx?dbcode=CAPJ&sfield=au&skey=朱艳辉&code=11283028"
    # url = "https://kns.cnki.net/kcms/detail/knetsearch.aspx?sfield=au&skey=%E5%8C%85%E7%8E%89%E5%B1%B1&code=08644430"
    # a = Author(url)
    a = Author()
    f = open("author.csv", 'a+', encoding='utf-8', newline="")
    # f_csv = csv.writer(f)
    # f_csv.writerow(('姓名', '学校', '专业', '总发布量', '总下载量', '专注领域', '作者文献', '导师', '学生'))
    a.save_csv(f)
