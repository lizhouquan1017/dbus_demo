# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_becomeClipboardOwner
# @Test Description:      设置当前剪切板所有者.
# @Test Condition:        无
# @Test Step:             1.调用BecomeClipboardOwner函数，设置当前剪切板所有者；
# @Test Result:           1.检查接口执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import clipboardManager
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用BecomeClipboardOwner函数，设置当前剪切板所有者")
        clipboardManager.becomeClipboardOwner()

    def tearDown(self):
        self.Step("收尾:无")
