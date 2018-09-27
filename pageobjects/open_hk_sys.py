# _*_ conding: utf - 8 _*_
from framework.base_page import Base_Page
from framework.logger import Logger
import time
from framework.browser_engine import Browser_Engine

logger = Logger(logger='Open_HK_sys').getloge()

class Open_HK_sys(Base_Page):
    wx_hk_btn = 'xpath=>//*[@id="ur_text_plane"]'  # 航空分组
    wx_hkairmaterial_btn = 'xpath=>//*[@id="td2"]/div[1]/img'  # 航材系统
    wx_hkcollector_btn = 'xpath=>//*[@id="td3"]/div[1]/img'  # 集装器系统
    wx_hkcost_btn = 'xpath=>//*[@id="td3"]/div[1]/img'  # 成本系统
    wx_hkssms_btn = 'xpath=>//*[@id="td5"]/div[1]/img'  #  结算管理系统

    def __init__(self, driver):
        self.driver = driver
    # 打开航空分组
    def open_hk(self):
        self.click(self.wx_hk_btn)
    # 打开航材系统
    def open_hkairmaterial(self):
        self.click(self.wx_hkairmaterial_btn)
        time.sleep(1)
        handle = Browser_Engine.handle(self.driver)
        handle.handle()
        time.sleep(1)

    # 打开集装器系统
    def open_khcollector(self):
        self.click(self.wx_hkcollector_btn)
        time.sleep(1)
        handle = Browser_Engine.handle(self.driver)
        handle.handle()
        time.sleep(1)
    # 打开成本系统
    def open_hkcost(self):
        self.click(self.wx_hkcost_btn)
        time.sleep(1)
        handle = Browser_Engine.handle(self.driver)
        handle.handle()
        time.sleep(1)
    # 打开结算管理系统
    def open_hkssms(self):
        self.click(self.wx_hkssms_btn)
        time.sleep(1)
        handle = Browser_Engine.handle(self.driver)
        handle.handle()
        time.sleep(1)