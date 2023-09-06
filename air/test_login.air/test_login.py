# -*- encoding=utf8 -*-
__author__ = "hello"

from airtest.core.api import *

from utils.common import get_window_handle
from utils.common import log

# window_handle = get_window_handle()
# connect_device("Windows:///" + str(window_handle))
# auto_setup(__file__)
# """
# 测试用例001：错误用户名和密码进行登录
# """
# try:
#     log.info("开始执行系统登录测试用例")
#     log.info("点击用户名输入框")
#     touch(Template(r"tpl1692768963122.png", record_pos=(-0.251, -0.023), resolution=(3840, 1080)))
#     log.info("输入用户名")
#     text("service")
#     log.info("点击密码输入框")
#     touch(Template(r"tpl1692769043752.png", record_pos=(-0.236, -0.005), resolution=(3840, 1080)))
#     log.info("输入密码")
#     text("service")
#     log.info("点击登录按钮")
#     touch(Template(r"tpl1692768882854.png", record_pos=(-0.253, 0.03), resolution=(3840, 1080)))
#     time.sleep(3)
#     log.info("判断主界面是否显示")
#     assert_exists(Template(r"tpl1693461231180.png", record_pos=(-0.433, -0.131), resolution=(3840, 1080)), "登录失败未进入主界面")
# except AssertionError as e:
#     log.error("Assertion failed:{}".format(e))
#     raise AssertionError
# except TargetNotFoundError as e:
#     log.error("Target not found:{}".format(e))
#     raise TargetNotFoundError

connect_device("Windows:///")

auto_setup(__file__)

log.info("系统登录功能测试")
try:
    log.info("点击用户名输入框")
    touch(Template(r"tpl1693986247079.png", record_pos=(-0.258, -0.023), resolution=(3840, 1080)))
    log.info("输入用户名")
    text("service")
    log.info("点击密码输入框")
    touch(Template(r"tpl1693986264124.png", record_pos=(-0.26, -0.005), resolution=(3840, 1080)))
    log.info("输入密码")
    text("service")
    touch(Template(r"tpl1693986279235.png", record_pos=(-0.251, 0.029), resolution=(3840, 1080)))
    sleep(1.0)
    assert_exists(Template(r"tpl1693986311195.png", record_pos=(-0.433, -0.131), resolution=(3840, 1080)), "请填写测试点")
except AssertionError as e:
    raise AssertionError
except TargetNotFoundError as e:
    raise TargetNotFoundError
