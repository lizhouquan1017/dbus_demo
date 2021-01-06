# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_writeContent
# @Test Description:      将剪切板内容写进文件(文件保存目录： /tmp/dde-session-daemon-clipboard）.
# @Test Condition:        无
# @Test Step:             1.调用WriteContent函数，将剪切板内容写进文件；
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
        self.Step("步骤1：调用WriteContent函数，将剪切板内容写进文件(文件保存目录")
        clipboardManager.writeContent()

    def tearDown(self):
        self.Step("收尾:无")
