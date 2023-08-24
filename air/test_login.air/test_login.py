# -*- encoding=utf8 -*-
__author__ = "hello"

from airtest.core.api import *
from configs.config import *
from utils.common import get_window_handle

window_handle = get_window_handle()

connect_device("Windows:///" + str(window_handle))
auto_setup(__file__)
"""
测试用例001：错误用户名和密码进行登录
"""
touch(Template(r"tpl1692768963122.png", record_pos=(-0.251, -0.023), resolution=(3840, 1080)))
text("service")
touch(Template(r"tpl1692769043752.png", record_pos=(-0.236, -0.005), resolution=(3840, 1080)))

text("service")

touch(Template(r"tpl1692768882854.png", record_pos=(-0.253, 0.03), resolution=(3840, 1080)))
time.sleep(3)

"""
测试用例002：正确用户名和密码进行登录
"""

touch(Template(r"tpl1692768963122.png", record_pos=(-0.251, -0.023), resolution=(3840, 1080)))
text("service123")
touch(Template(r"tpl1692769043752.png", record_pos=(-0.236, -0.005), resolution=(3840, 1080)))

text("service123")

touch(Template(r"tpl1692768882854.png", record_pos=(-0.253, 0.03), resolution=(3840, 1080)))

