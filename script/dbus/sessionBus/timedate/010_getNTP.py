# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_getNTP
# @Test Description:      获取NTP属性值
# @Test Condition:
# @Test Step:             1.获取NTP属性值；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取NTP属性值并检查获取成功")
        timedate.getNTP()

    def tearDown(self):
        self.Step("收尾:无")
