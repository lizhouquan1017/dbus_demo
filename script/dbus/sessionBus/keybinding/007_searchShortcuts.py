# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_searchShortcuts
# @Test Description:      用于根据关键字查找快捷键.
# @Test Condition:        无
# @Test Step:             1.根据关键字查找快捷键，返回快捷键String类型数据；
# @Test Result:           1.返回String类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import keybinding
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.query = "窗口截图"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：根据关键字查找快捷键，返回String类型数据")
        keybinding.searchShortcuts(self.query)

    def tearDown(self):
        self.Step("收尾:无")
