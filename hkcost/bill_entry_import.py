# _*_ coding: utf - 8 _*_
from framework.base_page import Base_Page
from framework.browser_engine import Browser_Engine
from framework.logger import Logger
from framework.update_excel import Update_Excel
from framework.updoadfile import UpLoadFile
import time

logger = Logger(logger='').getloge()

class Bill_Entry_Import(Base_Page):
    """
    账单录入页面导入模块
    """
    be_imp_btn = 'xpath=>//*[@id="button-1140-btnInnerEl"]' # 导入按钮
    bei_upload_btn = 'xpath=>//*[@id="filefield-1194-buttonEl"]' # 上传按钮
    bei_smt_btn = 'xpath=>//*[@id="button-1197-btnInnerEl"]' # 提交按钮
    bei_dm_btn = 'xpath=>//*[@id="button-1005-btnInnerEl"]' # 导入成功确认按钮  //*[@id="button-1005-btnInnerEl"]

    def __init__(self, driver):
        self.driver = driver
    def import_sys_bill(self, sys_number):
        self.click(self.be_imp_btn)
        time.sleep(1)
        self.click(self.bei_upload_btn)
        time.sleep(1)
        file = 'C:\\Users\\songyufang\\PycharmProjects\\HKCostPlatformTest\\framework\\账单信息导入模板.xls'
        value = sys_number
        outputfile = 'output.xlsx'
        chf = Update_Excel()
        chf.update_hkcost_sysbill3(file, value, outputfile)
        time.sleep(1)
        file_path = 'C:\\Users\\songyufang\\PycharmProjects\\HKCostPlatformTest\\testsuits\\output.xlsx'
        upload_file = UpLoadFile()
        upload_file.upload_file(file_path)
        self.click(self.bei_smt_btn)
        time.sleep(5)
        self.click(self.bei_dm_btn)



