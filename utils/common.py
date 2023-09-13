# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/8/22 14:45
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : common.py
# @Software : PyCharm
import os.path
import subprocess
import configparser
import psutil
import pyautogui
import win32gui
import cv2 as cv
from airtest.core.api import connect_device

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
    # window_handle = get_window_handle()
    try:
        connect_device("Windows:///" + str(window_handle))
        print(f"句柄{window_handle}:窗口链接成功")
    except Exception as e:
        raise Exception("链接窗口失败:" + str(e))


def reconnect_window():
    """
    自动获取重新获取窗口句柄进行重连
    :return:
    """
    try:
        current_handle = get_window_handle()
        connect_to_window(current_handle)
    except Exception as e:
        raise Exception("重新链接窗口失败")


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


def clear_folder(folder_path):
    """
    清空文件夹中的文件
    :param folder_path:
    :return:
    """
    try:
        # 检查文件夹是否存在
        if not os.path.isdir(folder_path):
            print(f"路径 {folder_path} 不是一个文件夹.")
            return

        # 获取文件夹中的文件列表
        files = os.listdir(folder_path)

        # 如果文件夹为空，则不进行任何处理
        if len(files) == 0:
            print(f"文件夹 {folder_path} 为空，不需要删除文件.")
            return

        # 遍历文件列表，删除每个文件
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"已删除文件: {file_path}")
        print("文件删除成功.")
    except Exception as e:
        print(f"删除文件出错: {str(e)}")


def get_config_value(config_file_path, section, field):
    """
    读取配置文件获取用户信息学
    :param config_file_path:配置文件路径
    :param section:USER or PASSWORD
    :param field:username or password
    :return: 用户名或密码
    """
    # 创建一个ConfigParser对象
    config = configparser.ConfigParser()

    # 读取配置文件并指定编码为GBK
    try:
        config.read(config_file_path, encoding='utf-8')
    except FileNotFoundError:
        return None

    # 检查配置文件中是否存在指定的节和字段
    if section in config and field in config[section]:
        return config[section][field]

    return None

if __name__ == '__main__':
    # window_title = "LoginWindow"
    # window_handle = get_window_handle(window_title)
    # connect_to_window(window_handle)
    # time.sleep(5)
    # print(judge_image_exist("test_login"))
    # print(cv.__version__)
    # while True:
    #     time.sleep(2)
    # handle = get_window_handle()
    # print(handle)
    # print(win32gui.FindWindow(None,"LoginWindow"))

    # handle = get_window_handle()
    # connect_to_window(handle)
    # reconnect_window()
    clear_folder(report_path)
    # print(get_config_value(user_info_path, "USER", "username"))
