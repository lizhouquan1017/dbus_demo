# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_enableDevSignalRec
# @Test Description:      启用网络，检查是否接收到触发信号
# @Test Condition:
# @Test Step:             1.启用网络；
# @Test Result:           1.检查是否接收到触发信号;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import sNetwork


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.netPath = self.get_data('netPath')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:启用信号，并检查信号接收成功")
        sNetwork.enableDevSignalRec(self.netPath)

    def tearDown(self):
        self.Step("收尾:无")
