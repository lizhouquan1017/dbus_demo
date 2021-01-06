# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_pingNormalIP
# @Test Description:      ping正常ip地址
# @Test Condition:
# @Test Step:             1.输入正确IP地址；
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
        self.normalIp = self.get_data('normalIp')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:ping正常ip地址")
        sNetwork.ping(self.normalIp)

        self.CheckPoint("检查点1:检查输出内容正常")
        sNetwork.checkPingStatus(self.normalIp, 'normal')

    def tearDown(self):
        self.Step("收尾:无")
