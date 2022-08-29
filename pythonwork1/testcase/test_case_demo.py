# import os
import pytest
# from selenium import webdriver

# from base.log import llog
from getdata.getdataa import Getdata
from login_page.loginpage import loginpagecl
import time
from base.basepage import *

logger = llog()
class TestCases:
    @pytest.mark.parametrize('data', Getdata().get('../data/logindata.yaml'))
    def test_login(self, data):
        driver = webdriver.Firefox()
        login1 = loginpagecl(driver)
        login1.login(data['username'], data['pwd'])
        logger.info('正在校验中')
        driver.implicitly_wait(6)
        a = login1.gettext()
        assert a == data['text'] , login1.quit1()
        logger.info('校验成功')
        driver.quit()


if __name__ == '__main__':
    # date1=time.time()
    pytest.main(['-sv', '--capture=sys', '--html=../report/report.html'])
    # date2=time.time()
    # print(date2-date1) 报告中有运行时间

    # pytest.main(['-sv', '--alluredir=./report'])
    # os.system('allure generate --clean %s -o %s'%('./report','./report.html'))

