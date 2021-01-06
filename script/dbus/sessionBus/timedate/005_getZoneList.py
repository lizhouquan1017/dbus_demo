# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_getZoneList
# @Test Description:      获取区域时间列表
# @Test Condition:
# @Test Step:             1.获取区域时间列表；
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
        self.Step("步骤1:获取区域时间列表，检查获取成功")
        timedate.getZoneList()

    def tearDown(self):
        self.Step("收尾:无")
