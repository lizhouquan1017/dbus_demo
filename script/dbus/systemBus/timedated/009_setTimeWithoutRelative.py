# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_setTimeWithoutRelative
# @Test Description:      设置当前时间和日期
# @Test Condition:
# @Test Step:             1.设置当前时间和日期；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import timedated


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:关闭自动同步")
        timedated.setNTP(False, '')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置当前时间和日期，并检查设置成功")
        timedated.setTime(1595505311000000, False, '')

    def tearDown(self):
        self.Step("收尾:开启自动同步")
        timedated.setNTP(True, '')
