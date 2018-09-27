# _*_ coding: utf -8 _*_
from framework.logger import Logger
from framework.browser_engine import Browser_Engine
from framework.base_page import Base_Page
from pageobjects.login import Login
from hkcost.open_table import Open_hkcost_table
from hkcost.bill_entry_new import Bill_Entry_New
from hkcost.bill_entry_import import Bill_Entry_Import
from hkcost.bill_entry_query import Bill_Entry_Quert
import unittest
import time

logger = Logger(logger='').getloge()

class Hkcost_Bill_New(unittest.TestCase):
    def setUp(self):
        browser = Browser_Engine(self)
        self.driver = browser.open_browser(self)
    def testhkcost_bill_new(self):
        login_hkcost = Login(self.driver)
        login_hkcost.login_hkcost('成本')
        time.sleep(1)
        handle = Browser_Engine(self.driver)
        handle.handle()
        time.sleep(1)
        open_table =Open_hkcost_table(self.driver)
        open_table.open_hkcost_table('账单录入')
        # login_hkcost.click_hkcosttable1_btn()
        time.sleep(1)
        # open_table.iframe('views/bill/billIndex.jsp')
        open_new_page = Bill_Entry_New(self.driver)
        num = open_new_page.type_new_bill('普通账单', '20000')
        import_system_bill = Bill_Entry_Import(self.driver)
        import_system_bill.import_sys_bill(num)
        time.sleep(1)
        query_bill = Bill_Entry_Quert(self.driver)
        query_bill.be_input_bn(num)
        query_bill.be_click_tqy()
    def tearDown(self):
        self.driver.close()
        logger.info("close browser")
if __name__ == '__main__':
    unittest.main()



