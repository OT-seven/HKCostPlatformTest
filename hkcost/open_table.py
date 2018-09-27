# _*_ coding:utf - 8 _*_
from framework.base_page import Base_Page
from framework.logger import Logger
import time
from framework.browser_engine import Browser_Engine

logger = Logger(logger='Open_hkcost_table').getloge()

class Open_hkcost_table(Base_Page):
    hkcost_btif = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[4]/td/div'  #  业务类型信息
    hkcost_fiif = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[5]/td/div'  #  费目信息
    hkcost_sif = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[6]/td/div'   #  供应商信息
    hkcost_cif = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[7]/td/div'   #  合同信息 //*[@id="treeview-1076"]/table/tbody/tr[12]/td/div
    hkcost_fpif = 'xpath=>//*[@id="ext-gen1266"]/td/div'  #  费目价格信息
    hkcost_bepg = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[12]/td/div'  #  账单录入
    hkcost_brpg = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[12]/td/div'  #  商务审核
    hkcost_fapg = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[13]/td/div'  #  财务审核
    hkcost_pmpg = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[15]/td/div'  #  款项支付
    hkcost_cqpg = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[16]/td/div'  #  款项核销查询
    hkcost_lqpg = 'xpath=>//*[@id="ext-gen1272"]/div'  #  日志查询
    hkcost_psmpg = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[19]/td/div'  #  权限管理
    hkcost_ddpg = 'xpath=>//*[@id="treeview-1076"]/table/tbody/tr[20]/td/div'   #  数据字典

    def __init__(self, driver):
        self.driver = driver

    def open_hkcost_table(self, table_name):
        if table_name == '业务类型信息':
            # 打开业务类型信息页面
            self.click(self.hkcost_btif)
            self.driver.switch_to.frame('views/base/bussTypeIndex.jsp')
            time.sleep(1)
        elif table_name == '费目信息':
            # 打开费目信息页面
            self.click(self.hkcost_fiif)
            self.driver.switch_to.frame('views/fee/feeInfoIndex.jsp')
            time.sleep(1)
        elif table_name == '供应商信息':
            # 打开供应商信息页面
            self.click(self.hkcost_sif)
            self.driver.switch_to.frame('views/supplier/SupplierInfoIndex.jsp')
            time.sleep(1)
        elif table_name == '合同信息':
            # 打开合同信息页面
            self.click(self.hkcost_cif)
            self.driver.switch_to.frame('views/agreement/AgreementinfoIndex.jsp')
            time.sleep(1)
        elif table_name == '费目价格信息':
            # 打开费目价格信息页面
            self.click(self.hkcost_fpif)
            self.driver.switch_to.frame('views/feeprice/feePriceIndex.jsp')
            time.sleep(1)
        elif table_name == '账单录入':
            # 打开账单录入页面
            self.click(self.hkcost_bepg)
            self.driver.switch_to.frame('views/bill/billIndex.jsp')
            time.sleep(1)
        elif table_name == '商务审核':
            # 打开商务审核页面
            self.click(self.hkcost_brpg)
            self.driver.switch_to.frame('views/bill/billBussIndex.jsp')
            time.sleep(1)
        elif table_name == '财务审核':
            # 打开财务审核页面
            self.click(self.hkcost_fapg)
            self.driver.switch_to.frame('views/bill/billCostIndex.jsp')
            time.sleep(1)
        elif table_name == '款项支付':
            # 打开款项支付页面
            self.click(self.hkcost_pmpg)
            self.driver.switch_to.frame('views/pay/payInfoIndex.jsp')
            time.sleep(1)
        elif table_name == '款项核销查询':
            # 打开款项核销查询页面
            self.click(self.hkcost_cqpg)
            self.driver.switch_to.frame('views/checkpay/checkPayIndex.jsp')
            time.sleep(1)
        elif table_name == '日志查询':
            # 打开日志查询页面
            self.click(self.hkcost_lqpg)
            self.driver.switch_to.frame('views/system/logInformIndex.jsp')
            time.sleep(1)
        elif table_name == '权限管理':
            # 打开权限管理页面
            self.click(self.hkcost_psmpg)
            self.driver.switch_to.frame('views/role/Role_distribution.jsp')
            time.sleep(1)
        elif table_name == '数据字典':
            # 打开数据字典页面
            self.click(self.hkcost_ddpg)
            self.driver.switch_to.frame('views/system/LSclass.jsp')
            time.sleep(1)
        else:
            print('没有找到该页面')