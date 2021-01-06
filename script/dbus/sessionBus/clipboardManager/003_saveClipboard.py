# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_saveClipboard
# @Test Description:      保存剪切板数据.
# @Test Condition:        无
# @Test Step:             1.调用SaveClipboard函数，保存剪切板数据；
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
        self.Step("步骤1：调用SaveClipboard函数，保存剪切板数据")
        clipboardManager.saveClipboard()

    def tearDown(self):
        self.Step("收尾:无")
