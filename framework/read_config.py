# _*_ coding: utf - 8 _*_
import os
import configparser

class Read_Config(object):
    config = configparser.ConfigParser()
    config_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
    config.read(config_path)
    def choose_browser(browsername):
        browser = Read_Config.config.get('BrowserType', browsername)
        return browser

    def choos_url(URL):
        url = Read_Config.config.get('testserver', URL)
        return url

    def input_account(accountname):
        account = Read_Config.config.get('Account', accountname)
        return account

    def input_password(pwd):
        password = Read_Config.config.get('Password', pwd)
        return password
