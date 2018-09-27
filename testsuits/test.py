# _*_ coding: utf - 8 _*_
import time
from selenium import webdriver
from framework.updoadfile import UpLoadFile
from framework.update_excel import Update_Excel
from framework.browser_engine import Browser_Engine

import win32con
# 创建handle
d = webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(2)
# 输入地址
d.get("http://10.1.2.194:4028/hkcost/?src=UnitopWX")
time.sleep(2)
# 输入账号
d.find_element_by_id("username_ipt").send_keys("0018330")
# 输入密码
d.find_element_by_id("password_ipt").send_keys("qqqqqq")
# 点击登录按钮
d.find_element_by_xpath('//*[@id="fm1"]/div[3]/div[6]').click()
time.sleep(2)
# # 点击进入‘业务类型信息’页面
# d.find_element_by_xpath('//*[@id="treeview-1076"]/table/tbody/tr[4]/td/div').click()
# time.sleep(2)
# 切换iframe
# d.switch_to.frame("views/base/bussTypeIndex.jsp")
#点击进入‘账单录入’页面
d.find_element_by_xpath('//*[@id="treeview-1076"]/table/tbody/tr[12]/td/div').click()
# 切换iframe
iframe = 'views/bill/billIndex.jsp'
switch_to_iframe = Browser_Engine(d)
switch_to_iframe.iframe(iframe)

# d.switch_to.frame("views/bill/billIndex.jsp")
time.sleep(1)
# 点击新增按钮
d.find_element_by_xpath('//*[@id="button-1139-btnInnerEl"]').click()
time.sleep(2)
# 打开账单类型选择框
d.find_element_by_xpath('//*[@id="ext-gen1579"]').click()
time.sleep(2)
# 选择账单类型
d.find_element_by_xpath('//*[@id="boundlist-1220-listEl"]/ul/li[1]').click()
time.sleep(2)

# 获取供应商账单编号
try:
    num = d.find_element_by_id('add_2-inputEl').get_attribute("value")
    print (num)
except Exception as e:
    print("获取供应商账单编号失败")
time.sleep(2)
# 打开结算供应商选择框
d.find_element_by_xpath('//*[@id="ext-gen1584"]').click()
time.sleep(2)
# 选择结算供应商
d.find_element_by_xpath(' //*[@id="boundlist-1222-listEl"]/ul/li[8]').click()
time.sleep(2)
# 打开账单开始日期选择框
d.find_element_by_xpath('//*[@id="ext-gen1588"]').click()
time.sleep(2)
# 选择账单开始日期
d.find_element_by_xpath('//*[@id="datepicker-1224-prevEl"]').click()
d.find_element_by_xpath('//*[@id="ext-gen1634"]').click()
time.sleep(2)
# 打开账单结束日期选择框
d.find_element_by_xpath('//*[@id="ext-gen1591"]').click()
time.sleep(2)
# 选择账单结束日期
d.find_element_by_xpath('//*[@id="ext-gen1711"]').click()
time.sleep(2)
# 打开币种选择框
d.find_element_by_xpath('//*[@id="ext-gen1594"]').click()
time.sleep(2)
# 选择币种  //*[@id="boundlist-1230-listEl"]/ul/li[14]   //*[@id="boundlist-1230-listEl"]/ul/li[14]
d.find_element_by_tag_name('CNY').click()
time.sleep(2)
# 输入结算总价  //*[@id="add_7-inputEl"]
d.find_element_by_xpath('//*[@id="add_7-inputEl"]').send_keys('20000')
time.sleep(2)
# 点击保存按钮
d.find_element_by_xpath('//*[@id="button-1186-btnInnerEl"]').click()
time.sleep(2)
# 点击确定按钮，关闭新增成功提示框
d.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
time.sleep(2)
# 查询框输入供应商账单编号
d.find_element_by_xpath('//*[@id="search_1-inputEl"]').send_keys(num)
time.sleep(2)
# 点击查询按钮
d.find_element_by_xpath('//*[@id="serch-btnInnerEl"]').click()
time.sleep(2)
file = 'C:\\Users\\songyufang\\PycharmProjects\\HKCostPlatformTest\\framework\\账单信息导入模板.xls'
value = num
outputfile = 'output.xlsx'
sysbill_file = Update_Excel()
sysbill_file.update_hkcost_sysbill3(file, value, outputfile)
# upload_sysbill = UpLoadFile()
# upload_sysbill.upload_file('C:\\Users\\songyufang\\PycharmProjects\\HKCostPlatformTest\\framework\\output.xls')

# 点击导入
d.find_element_by_xpath('//*[@id="button-1140-btnInnerEl"]').click()
time.sleep(2)
d.find_element_by_xpath('//*[@id="filefield-1194-buttonEl"]').click()
time.sleep(2)
UpLoadFile.upload_file('C:\\Users\\songyufang\\PycharmProjects\\HKCostPlatformTest\\testsuits\\output.xlsx')
# UpLoadFile.upload_file('C:\\Users\\songyufang\\Desktop\\导入\\账单信息导入模板.xlsx')

#点击提交按钮
d.find_element_by_xpath('//*[@id="button-1197-btnInnerEl"]').click()
time.sleep(5)


# 退出
d.quit()


