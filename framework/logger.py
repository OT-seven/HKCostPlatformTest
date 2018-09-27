# _*_ coding = utf - 8 _*_
import logging
import time
import os.path

class Logger(object):
    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志保存到指定的文件中
        :param logger:
        """

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handle，用于写入日志
        rp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_name = log_path + rp + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        #再创建一个handle，用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handle的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handle
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getloge(self):
        return self.logger