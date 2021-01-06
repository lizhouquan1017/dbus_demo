# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_setGreeterBackground
# @Test Description:
# @Test Condition:
# @Test Step:             1.设置欢迎界面背景；
# @Test Result:           1.检查设置欢迎界面背景成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import os
import platform
import logging

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import user
from aw.dbus.systemBus import accounts


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.passwd = self.get_data('passwd')
        self.username = self.get_data('username')
        self.gre_background = self.get_data('gre_background')

        if 'mips64'==platform.machine():
            self.gre_background = f"{os.path.splitext(self.gre_background)[0]}{'.bmp'}"

        self.Step("预制条件2:删除账户")
        accounts.deleteUser(self.passwd, self.username)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置欢迎界面背景")
        user.setGreeterBackground(self.passwd, self.username, self.gre_background)

        self.CheckPoint("检查点1：检查设置欢迎界面背景成功")
        user.checkGreeterBackground(self.passwd, self.username, self.gre_background)

    def tearDown(self):
        self.Step("收尾:")
        accounts.deleteUser(self.passwd, self.username)
