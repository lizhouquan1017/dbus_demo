# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_setLongPressDuration
# @Test Description:      设置手势触屏事件时间上限
# @Test Condition:
# @Test Step:             1.执行SetLongPressDuration(uint32 duration) -> ()，传入参数为700ms；
# @Test Result:           1.设置手势触屏事件时间上限成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import daemon


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:设置参数")
        self.duration = 700

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:执行SetLongPressDuration(uint32 duration) -> ()，传入参数为700ms,并检查设置成功")
        daemon.setLongPressDuration(self.duration)

    def tearDown(self):
        self.Step("收尾:无")
