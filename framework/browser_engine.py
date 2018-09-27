# _*_ coding:utf - 8 _*_
import os.path
from selenium import webdriver
from framework.logger import Logger
from framework.read_config import Read_Config

logger = Logger(logger='Browser_Engine').getloge()

class Browser_Engine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    firefox_driver_path = dir + '/tools/geckodriver.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        # config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        # config.read(file_path)

        browser = Read_Config.choose_browser('browsername')
        logger.info("you had select %s" % browser)
        url = Read_Config.choos_url("URL")
        logger.info("the test server url is %s" % url)

        if browser == "FireFox":
            driver = webdriver.Firefox()
            logger.info("starting firefox browser")
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("starting chrome browser")
        elif browser == "Ie":
            driver = webdriver.Ie()
            logger.info("starting ie browser")

        driver.get(url)
        logger.info("browser open %s" % url)
        driver.maximize_window()
        logger.info("maximize the current window")
        driver.implicitly_wait(3)
        logger.info(" set implicitly wait 3 seconds")
        return driver
    def handle(self):
        handles = self.driver.window_handles
        for handle in handles:  # 切换窗口
            if handle != self.driver.current_window_handle:
                print
                'switch to second window', handle
                self.driver.close()  # 关闭第一个窗口
                self.driver.switch_to.window(handle)
    def iframe(self, iframeid):
        self.driver.switch_to.frame(iframeid)
