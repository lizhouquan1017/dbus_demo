# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_pingErrorIp
# @Test Description:      ping错误ip地址
# @Test Condition:
# @Test Step:             1.输入错误IP地址；
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
        self.errorIp = self.get_data('errorIp')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:ping错误ip地址")
        sNetwork.ping(self.errorIp)

        self.CheckPoint("检查点1:检查输出内容正常")
        sNetwork.checkPingStatus(self.errorIp, 'error')

    def tearDown(self):
        self.Step("收尾:无")
