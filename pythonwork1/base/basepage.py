from . import log
from selenium import webdriver

logger = log.llog()


class basepagecl:
    def __init__(self, driver):
        self.driver = driver
        logger.info('实例传递驱动')

    # 进入页面
    def open(self, url):
        self.driver.get(url)
        logger.info('进入{}页面'.format(url))

    # 退出页面
    def quit1(self):
        self.driver.quit()
        logger.info('校验失败')

    # 定位元素
    def loctor(self, loct):
        try:
            return self.driver.find_element(*loct)
        except Exception as e:
            logger.error('未找到{}元素'.format(loct))

    # 输入
    def input(self, loct, text):
        self.loctor(loct).send_keys(text)
        logger.info('输入用户名或者密码{}'.format(text))

    # 点击
    def click(self, loct):
        try:
            self.loctor(loct).click()
        except Exception as e:
            logger.error('未找到点击元素错误{}'.format(e))
