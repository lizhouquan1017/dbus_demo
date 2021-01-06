# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_removeTarget
# @Test Description:      移除剪切板上指定信息.
# @Test Condition:        无
# @Test Step:             1.调用RemoveTarget函数，移除剪切板上指定信息；
# @Test Result:           1.检查接口执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import clipboardManager
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.target = 1

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用RemoveTarget函数，移除剪切板上指定信息")
        clipboardManager.removeTarget(self.target)

    def tearDown(self):
        self.Step("收尾:无")
