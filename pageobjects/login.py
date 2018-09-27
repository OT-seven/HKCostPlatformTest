# _*_ coding: utf - 8 _*_
from framework.base_page import Base_Page
from framework.logger import Logger
from framework.read_config import Read_Config
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

logger = Logger(logger='login').getloge()

class Login(Base_Page):
    wx_act_iputbox = 'id=>username_ipt'
    wx_pwd_iputbox = 'id=>password_ipt'
    wx_login_btn = 'xpath=>//*[@id="fm1"]/div[3]/div[6]'
    wx_hk_btn = 'xpath=>//*[@id="ur_text_plane"]'
    wx_hkcost_btn = 'xpath=>//*[@id="td1"]/div[1]/img'
    hkcost_table1 = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[12]/td/div'
    input_btn = 'xpath=>//*[@id="button-1093"]'


    def __init__(self, driver):
        self.driver = driver
    def login_hkcost(self,sys_name):
        hkcost_act = Read_Config.input_account('accountname')
        self.type(self.wx_act_iputbox, hkcost_act)
        logger.info('输入账号')
        hkcost_pwd = Read_Config.input_password('pwd')
        self.type(self.wx_pwd_iputbox, hkcost_pwd)
        logger.info('输入密码')
        self.driver.find_element_by_xpath('//*[@id="fm1"]/div[3]/div[6]').click()
        self.refresh()
        logger.info('刷新页面')
        self.click(self.wx_hk_btn)
        logger.info('点击万象航空组')
        if sys_name == '成本':
            self.click(self.wx_hkcost_btn)
            logger.info('点击打开航空成本系统')
        else:
            print('系统名称输入错误')


    def click_hkcosttable1_btn(self):
        self.click(self.hkcost_table1)
        logger.info('打开账单录入页签')
    def switch_to_frame(self):
        self.driver.switch_to.frame("views/feeprice/feePriceIndex.jsp")
    def click_input_btn(self):
        self.click(self.input_btn)
        logger.info('点击导入按钮')