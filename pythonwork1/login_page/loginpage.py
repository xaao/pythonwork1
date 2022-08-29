# import time
#
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.basepage import basepagecl


class loginpagecl(basepagecl):
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'

    username = (By.NAME, 'accounts')
    pwd = (By.NAME, 'pwd')
    button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
    def login(self,username1,pwd1):
        self.open(self.url)
        self.input(self.username,username1)
        self.input(self.pwd,pwd1)
        # self.input(Keys.CONTROL,'a')
        self.click(self.button)
    def gettext(self):
        try:
            return self.driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div[1]/div[1]/div[1]/div/span').text
        except Exception as e:
            print('error:{}'.format(e))