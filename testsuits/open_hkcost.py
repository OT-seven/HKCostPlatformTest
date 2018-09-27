# _*_ coding: utf -8 _*_
from framework.logger import Logger
from framework.browser_engine import Browser_Engine
from framework.base_page import Base_Page
from pageobjects.login import Login
import unittest
import time

logger = Logger(logger='Open_hkcost').getloge()

class Open_hkcost(unittest.TestCase):
    def setUp(self):
        browse = Browser_Engine(self)
        self.driver = browse.open_browser(self)
        logger.info("open browser")
    def test_login_hkcost(self):
        # 实例化
        login_hkcost = Login(self.driver)
        # 输入账号
        login_hkcost.input_act(self)
        time.sleep(2)
        logger.info("input account")
        # 输入密码
        login_hkcost.input_pwd(self)
        time.sleep(2)
        logger.info("input password")
        # 点击登录按钮
        # login_hkcost.click_login_btn()
        self.driver.find_element_by_xpath('//*[@id="fm1"]/div[3]/div[6]').click()
        time.sleep(2)
        logger.info("click the login btn")
        # 刷新页面
        login_hkcost.browser_refresh()
        time.sleep(2)
        # 点击航空分组按钮
        login_hkcost.click_wx_hk_btn()
        time.sleep(2)
        logger.info("click the hk btn")
        # 点击成本系统
        login_hkcost.click_wx_hkcost_btn()
        time.sleep(2)
        logger.info("click the hkcost btn")
        # 切换窗口handle
        handle = Browser_Engine(self.driver)
        handle.handle()
        time.sleep(2)
        logger.info("switch to new window")
        # 打开‘业务类型信息’页签
        login_hkcost.click_hkcosttable1_btn()
        time.sleep(2)
        logger.info("click the hkcosttable1")
        # 切换frame
        login_hkcost.switch_to_frame()
        time.sleep(2)
        logger.info("switch to frame")
        # 点击导入按钮
        login_hkcost.click_input_btn()
        # self.driver.find_element_by_xpath('//*[@id="button-1093"]').click()
        time.sleep(2)
        logger.info("click the input btn")

    def tearDown(self):
        self.driver.close()
        logger.info("close browser")
if __name__ == '__main__':
    unittest.main()