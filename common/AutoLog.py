#!/usr/bin/python3.6.1
"""
@author: huangsx
Created on 2016年6月28日
Updated on 2018年9月18日 【更新整理】
"""
import logging
import time


# --------------------------------------------------------------------------------------------------


class AutomationLog(object):
    """定义一个处理自动化测试过程中日志记录的类，包含以下方法：同时记录日志到控制台和文件"""

    @staticmethod
    def init_log():
        """重新定义log输出方法，实现将日志信息同时分别输出到日志文件和console控制台"""
        Logger = logging.getLogger()
        LogSavePath = '../log/'
        curren_time = time.strftime('%Y-%m-%d')
        LogSaveName = ' YSS-UI-Test.log'
        LogFileObject = LogSavePath+curren_time+LogSaveName
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - UAT:%(message)s',
                            filename=LogFileObject,  # 日志文件按天增量记录到log目录
                            filemode='a')
        console = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - UAT:%(message)s')
        console.setFormatter(formatter)
        Logger.addHandler(console)
        console.setLevel(logging.DEBUG)
        return [Logger, console]

    @staticmethod
    def LogMsg(err_msg, level=None):
        """实现同时输出日志到文件及控制台,level代表的是级别，err_msg代表日志信息"""
        logger, console = AutomationLog.init_log()
        if level == 0:
            logging.debug(err_msg)
        elif level == 1:
            logging.warning(err_msg)
        elif level == 2:
            logging.error(err_msg)
        elif level == 3:
            logging.critical(err_msg)
        else:
            logging.info(err_msg)
        logger.removeHandler(console)  # 清除log控制台句柄，防止日志重复输出

if __name__ == "__main__":
    for i in [0, 1, 2, 3, 4]:
        AutomationLog.LogMsg('日志测试', i)
