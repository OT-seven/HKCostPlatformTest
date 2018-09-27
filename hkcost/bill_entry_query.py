# _*_ coding: utf - 8 _*_
from framework.base_page import Base_Page
from framework.logger import Logger
import time

logger = Logger(logger='Bill_Entry_Quert').getloge()

class Bill_Entry_Quert(Base_Page):
    """
    账单录入页面查询操作
    """
    be_bs = 'xpath=>//*[@id="search_0-inputEl"]' # 账单状态输入框
    be_bn = 'xpath=>//*[@id="search_1-inputEl"]' # 账单编号输入框
    be_sms = 'xpath=>//*[@id="search_2-inputEl"]' # 结算供应商输入框
    be_bt0 = 'xpath=>//*[@id="ext-gen1468"]'  # 账单类型下拉按钮
    be_bt1 = 'xpath=>//*[@id="boundlist-1218-listEl"]/ul/li[1]' # 普通账单
    be_bt2 = 'xpath=>//*[@id="boundlist-1218-listEl"]/ul/li[2]' # 预付款账单
    be_std1 = 'xpath=>//*[@id="ext-gen1472"]' # 账单日期起选择器按钮
    be_std2 = 'xpath=>//*[@id="ext-gen1577"]/a/em/span' # 当月1号
    be_etd3 = 'xpath=>//*[@id="ext-gen1475"]'  # 账单日期止选择器按钮
    be_etd4 = 'xpath=>//*[@id="ext-gen1651"]/a/em/span'  # 当月30号
    be_otr = 'xpath=>//*[@id="search_6-inputEl"]' # 操作人输入框
    be_opt = 'xpath=>//*[@id="combobox-1136-inputEl"]' # 机场三字码输入框
    be_tqy_btn = 'xpath=>//*[@id="serch-btnInnerEl"]' # 查询按钮
    be_cst_btn = 'xpath=>//*[@id="button-1138-btnInnerEl"]' # 重置按钮

    def __init__(self, driver):
        self.driver = driver

    # 账单状态输入
    def be_input_bs(self, ip_be_bs):
        self.type(self.be_bs, ip_be_bs)
        time.sleep(1)
    # 账单编号输入
    def be_input_bn(self, ip_be_bn):
        self.type(self.be_bn, ip_be_bn)
        time.sleep(1)
    # 结算供应商输入
    def be_input_sms(self, ip_be_sms):
        self.type(self.be_sms, ip_be_sms)
        time.sleep(1)
    # 账单类型选择
    def be_input_bt(self, ip_be_bt):
        self.click(self.be_bt0)
        if ip_be_bt == '普通账单':
            self.click(self.be_bt1)
        elif ip_be_bt == '预付款账单':
            self.click(self.be_bt1)
        else:
            print('账单类型输入错误')
    # 选择账单日期起时间（选择当月1号）
    def be_input_std(self):
        self.click(self.be_std1)  # 点击时间选择器按钮
        time.sleep(1)
        self.click(self.be_std2)  # 选择当月1号
        time.sleep(1)
    # 选择账单日期止时间（选择当月30号）
    def be_input_etd(self):
        self.click(self.be_etd3)  # 点击时间选择器按钮
        time.sleep(1)
        self.click(self.be_etd4)  # 选择当月30号
        time.sleep(1)
    # 操作人输入
    def be_input_otr(self, ip_be_otr):
        self.type(self.be_otr, ip_be_otr)
        time.sleep(1)
    # 机场三字码输入
    def be_input_apt(self, ip_be_opt):
        self.type(self.be_opt, ip_be_opt)
        time.sleep(1)
    # 点击查询按钮
    def be_click_tqy(self):
        self.click(self.be_tqy_btn)
        time.sleep(1)
    # 点击重置按钮
    def be_click_cst(self):
        self.click(self.be_cst_btn)
        time.sleep(1)