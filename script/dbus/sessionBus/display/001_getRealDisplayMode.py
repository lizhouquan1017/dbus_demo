# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_getRealDisplayMode
# @Test Description:      获取显示器真实排列方式
# @Test Condition:
# @Test Step:             1.获取显示器真实排列方式；
# @Test Result:           1.检查获取显示器真实排列方式成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import display


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:打开一个网络连接")
        display.getRealDisplayMode()

    def tearDown(self):
        self.Step("收尾:")
