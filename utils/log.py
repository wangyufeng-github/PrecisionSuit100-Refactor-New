# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/5/18 14:57
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : handle_log.py
# @Software : PyCharm

import datetime
import logging

from configs.config import log_path


def logger(log_file_name, fileLog=True, name=__name__):
    """
    日志收集器
    :param log_file_name: 日志文件名
    :param name: 模块名称
    :return:
    """
    # 日志文件路径
    logDir = f'{log_path}/{log_file_name}.log'
    # 创建日志收集器对象
    logObject = logging.getLogger(name)
    # 设置日志级别为INFO
    logObject.setLevel(logging.INFO)
    # 设置日志内容的格式:时间+级别+行号+具体报错信息
    fmt = "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s[%(lineno)d]:%(message)s"
    formater = logging.Formatter(fmt)

    # 文件输出
    if fileLog:
        handle = logging.FileHandler(logDir, encoding='utf-8')
        handle.setFormatter(formater)
        logObject.addHandler(handle)
    # 控制台输出
    else:
        handle2 = logging.StreamHandler()
        handle2.setFormatter(formater)
        logObject.addHandler(handle2)

    return logObject


if __name__ == '__main__':
    log = logger('用户登录功能测试')
    log.info('我是示例日志')
