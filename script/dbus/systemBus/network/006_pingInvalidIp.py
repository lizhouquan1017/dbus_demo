# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_pingInvalidIp
# @Test Description:      ping无效ip地址
# @Test Condition:
# @Test Step:             1.输入无效IP地址；
# @Test Result:           1.检查输出;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import sNetwork


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.invalidIp = self.get_data('invalidIp')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:ping无效ip地址")
        sNetwork.ping(self.invalidIp)

        self.CheckPoint("检查点1:检查输出内容正常")
        sNetwork.checkPingStatus(self.invalidIp, 'invalid')

    def tearDown(self):
        self.Step("收尾:无")
