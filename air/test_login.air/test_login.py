# -*- encoding=utf8 -*-
__author__ = "hello"

import os.path
import pprint
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from airtest.core.api import *
from utils.log import logger
from configs.config import user_info_path
from utils.common import get_window_handle, get_config_value

user_name = get_config_value(user_info_path, "USER", "username")
password = get_config_value(user_info_path, "PASSWORD", "password")

log = logger("系统登录功能")
connect_device("Windows:///")
auto_setup(__file__)

log.info("系统登录功能测试")
try:
    log.info("点击用户名输入框")
    touch(Template(r"tpl1693986247079.png", record_pos=(-0.258, -0.023), resolution=(3840, 1080)))
    log.info("输入用户名%s" % user_name)
    text(user_name)
    log.info("点击密码输入框")
    touch(Template(r"tpl1693986264124.png", record_pos=(-0.26, -0.005), resolution=(3840, 1080)))
    log.info("输入密码%s" % password)
    text(password)
    log.info("点击登录按钮")
    touch(Template(r"tpl1693986279235.png", record_pos=(-0.251, 0.029), resolution=(3840, 1080)))
    sleep(1.0)
    log.info("成功进入病例管理界面")
    assert_exists(Template(r"tpl1693986311195.png", record_pos=(-0.433, -0.131), resolution=(3840, 1080)),
                  "病例管理界面断言的控件未找到！")
except AssertionError as e:
    log.error(e)
    raise AssertionError
except TargetNotFoundError as e:
    log.error(e)
    raise TargetNotFoundError
