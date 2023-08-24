# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/8/22 14:45
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : common.py
# @Software : PyCharm
import os.path
import time

import cv2 as cv
import subprocess

import pyautogui
import win32gui
import win32con
import pygetwindow as gw
from airtest.core.api import connect_device
import win32gui
import psutil
from configs.config import *


def get_window_handle():
    """
    获取窗口句柄
    :param window_title:
    :return:
    """
    try:
        hwnd = win32gui.FindWindow(None, "LoginWindow")
        if hwnd == 0:
            hwnd = win32gui.FindWindow(None, "PrecisionSuit100")
        return hwnd
    except Exception:
        raise Exception("windows handle is not found!")


def connect_to_window(window_handle):
    """
    利用句柄链接窗口
    :param window_handle:
    :return:
    """
    try:
        connect_device("Windows:///" + str(window_handle))
        print("链接窗口成功")
    except Exception as e:
        raise Exception("链接窗口失败:" + str(e))


def kill_process_by_name(process_name):
    """
    通过进程名关闭应用程序
    :param process_name:
    :return:
    """
    for proc in psutil.process_iter():
        try:
            if proc.name() == process_name:
                proc.kill()
        except psutil.NoSuchProcess:
            pass


def start_application(app_path):
    """
    启动应用程序
    :param app_path:
    :return:
    """
    try:
        command = 'tasklist /FI "IMAGENAME eq {}" /NH'.format(app_process_name)
        output = subprocess.check_output(command, shell=True)
        output_str = output.decode('gbk')
        if app_process_name in output_str:
            kill_process_by_name(app_process_name)
        else:
            subprocess.Popen(app_path, cwd=os.path.dirname(app_path))
    except subprocess.CalledProcessError:
        pass


def judge_image_exist(templateImage, confidencevalue=0.7):
    """
    通过截取当前屏幕，判断模板图片是否在当前屏幕中
    :param self:
    :param templateImage:
    :param confidencevalue:
    :return:
    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\image\\"
    image = pyautogui.screenshot()
    image.save(f'{path}screenshot\screen.png')
    obj_image = cv.imread(f'{path}screenshot\screen.png')
    template_path = f'{path}template\{templateImage}.png'
    template = cv.imread(template_path)
    # 调用matchTemplate方法进行匹配
    result = cv.matchTemplate(obj_image, template, cv.TM_CCOEFF_NORMED)
    # 匹配度
    similarity = cv.minMaxLoc(result)[1]
    if similarity < confidencevalue:
        return False
    else:
        return True


if __name__ == '__main__':
    # window_title = "LoginWindow"
    # window_handle = get_window_handle(window_title)
    # connect_to_window(window_handle)
    # time.sleep(5)
    # print(judge_image_exist("tpl1692772230855"))
    # while True:
    #     time.sleep(2)
    handle = get_window_handle()
    print(handle)
    # print(win32gui.FindWindow(None,"LoginWindow"))
