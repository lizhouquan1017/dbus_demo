# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_setDisableNTP
# @Test Description:      设置不使用NTP
# @Test Condition:
# @Test Step:             1.设置不使用NTP；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:设置使用NTP")
        timedate.setNTP(True)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置不使用NTP")
        timedate.setNTP(False)

        self.CheckPoint("检查点1：检查设置成功")
        timedate.checkNTPStatus('disable')

    def tearDown(self):
        self.Step("收尾:设置使用NTP")
        timedate.setNTP(True)
