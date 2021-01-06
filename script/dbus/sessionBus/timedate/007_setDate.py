# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_setDate
# @Test Description:      设置系统时间和日期
# @Test Condition:        关闭时间自动同步设置
# @Test Step:             1.重置系统时间和网络时间同步；
# @Test Result:           1.检查重置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:关闭时间自动同步设置")
        timedate.setNTP(False)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置系统时间和日期")
        timedate.setDate(2020, 7, 28, 10, 30, 10, 0)

        self.CheckPoint("检查点1: 检查时间设置成功")
        timedate.checkSetDateStatus(7, 28)

    def tearDown(self):
        self.Step("收尾:还原系统时间设置")
        time.sleep(2)
        timedate.reset()