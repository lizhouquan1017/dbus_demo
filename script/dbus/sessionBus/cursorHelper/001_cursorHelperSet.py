# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_cursorHelperSet
# @Test Description:      设置光标的主题name.
# @Test Condition:        无
# @Test Step:             1.设置光标的主题name；
# @Test Result:           1.检查执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import cursorHelper
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.cursor_name = "name"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置光标的主题name")
        cursorHelper.cursorHelperSet(self.cursor_name)

    def tearDown(self):
        self.Step("收尾:无")
