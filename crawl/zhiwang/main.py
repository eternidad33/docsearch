import time

from crawl.zhiwang import zhiwang

if __name__ == "__main__":
    driver = zhiwang.loadDriver()
    key = "知识图谱"
    zhiwang.inputKeyword(driver, key)
    time.sleep(3)
    zhiwang.getArticle(driver)
