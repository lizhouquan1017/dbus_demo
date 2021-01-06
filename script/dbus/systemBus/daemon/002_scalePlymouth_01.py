# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_scalePlymouth_01
# @Test Description:      设置开机启动图形主题
# @Test Condition:
# @Test Step:             1.执行ScalePlymouth(uint32 scale) -> ()，传入参数为1；
# @Test Result:           1.检查设置开机启动图形主题为uos-ssd-logo成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import daemon


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:设置参数")
        self.scale = 1

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:执行ScalePlymouth(uint32 scale) -> ()，传入参数为1")
        daemon.scalePlymouth(self.scale)

        self.Step("检查点1：检查设置开机启动图形主题为uos-ssd-logo成功")
        daemon.checkScalePlymouth(self.scale)

    def tearDown(self):
        self.Step("收尾:无")
