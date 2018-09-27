# _*_ coding: utf - 8 _*_
import win32con
import win32api
import win32gui
from framework.logger import Logger
import time

logger = Logger(logger='UpLoadFile').getloge()

class UpLoadFile(object):
    @staticmethod
    def upload_file(file_path):
        dialog = win32gui.FindWindow('#32770', u'打开')
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(Edit, 0, 'button', None)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file_path)
        time.sleep(2)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        time.sleep(2)
