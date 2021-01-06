# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_langSelectorReset
# @Test Description:      将设置的用户桌面语言环境重置为系统默认语言环境.
# @Test Condition:        无
# @Test Step:             1.调用Reset函数，将设置的用户桌面语言环境重置为系统默认语言环境；
# @Test Result:           1.检查接口执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import langSelector
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用Reset函数，将设置的用户桌面语言环境重置为系统默认语言环境")
        langSelector.langSelectorReset()

    def tearDown(self):
        self.Step("收尾:无")
