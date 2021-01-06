# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_getSourcePorts
# @Test Description:      获取支持的输出端口
# @Test Condition:
# @Test Step:             1.获取支持的输出端口；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audioSource


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取支持的输出端口，并检查获取成功")
        audioSource.getSourcePorts()

    def tearDown(self):
        self.Step("收尾:无")
