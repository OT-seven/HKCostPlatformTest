# _*_ coding: utf - 8 _*_
from framework.base_page import Base_Page
from framework.logger import Logger
import time

logger = Logger(logger='').getloge()

class Bill_Entry_New(Base_Page):
    """
    账单录入页面新增操作
    """
    be_new_btn = 'xpath=>//*[@id="button-1139-btnInnerEl"]'  # 新增按钮
    ben_bt01 = 'xpath=>//*[@id="ext-gen1579"]' # 新增页面账单类型下拉按钮
    ben_bt02 = 'xpath=> //*[@id="boundlist-1220-listEl"]/ul/li[1]'  # 普通账单
    ben_bt03 = 'xpath=>//*[@id="boundlist-1220-listEl"]/ul/li[2]'  # 预付款账单
    ben_sms01 = 'xpath=>//*[@id="ext-gen1584"]'  # 结算供应商下拉按钮
    ben_sms02 = 'xpath=>//*[@id="boundlist-1222-listEl"]/ul/li[8]'  # 选择结算供应商
    ben_std01 = 'xpath=>//*[@id="ext-gen1588"]' # 账单日期起选择器按钮
    ben_std02 = 'xpath=>//*[@id="ext-gen1664"]/a/em/span' # 当月1号
    ben_std03 = 'xpath=>//*[@id="ext-gen1591"]' # 账单日期止选择器按钮
    ben_std04 = 'xpath=>//*[@id="ext-gen1711"]/a/em/span' # 当月30号
    ben_cry01 = 'xpath=>//*[@id="ext-gen1594"]' # 币种下拉按钮
    ben_cry02 = 'xpath=>//*[@id="boundlist-1230-listEl"]/ul/li[14]' # 选择人民币
    ben_smp = 'xpath=>//*[@id="add_7-inputEl"]' # 结算总价输入框
    ben_sysbn = 'xpath=>//*[@id="add_2-inputEl"]' # 供应商账单编号
    ben_save_btn = 'xpath=>//*[@id="button-1186-btnInnerEl"]' # 保存按钮
    ben_dm_btn = 'xpath=>//*[@id="button-1005-btnInnerEl"]' # 点击确定按钮，关闭新增成功提示框


    def __init__(self, driver):
        self.driver = driver
    def type_new_bill(self, bill_type, total_price):
        self.click(self.be_new_btn)
        time.sleep(1)
        self.click(self.ben_bt01)
        time.sleep(1)
        if bill_type == '普通账单':
            self.click(self.ben_bt02)
        elif bill_type == '预付款账单':
            self.click(self.ben_bt03)
        else:
            print('账单类型输入错误')
        time.sleep(1)
        self.click(self.ben_sms01)
        time.sleep(1)
        self.click(self.ben_sms02)
        time.sleep(1)
        self.click(self.ben_std01)
        time.sleep(1)
        self.click(self.ben_std02)
        time.sleep(1)
        self.click(self.ben_std03)
        time.sleep(1)
        self.click(self.ben_std04)
        time.sleep(1)
        self.click(self.ben_cry01)
        time.sleep(1)
        self.click(self.ben_cry02)
        time.sleep(1)
        self.type(self.ben_smp, total_price)
        sys_bill_num = self.get_page_num(self.ben_sysbn)
        print(sys_bill_num)
        self.click(self.ben_save_btn)
        self.click(self.ben_dm_btn)
        return sys_bill_num