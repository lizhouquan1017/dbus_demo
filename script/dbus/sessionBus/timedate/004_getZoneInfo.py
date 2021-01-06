# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_getZoneInfo
# @Test Description:      获得时间区域相关信息
# @Test Condition:
# @Test Step:             1.获得时间区域相关信息；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.zone = 'Asia/Shanghai'

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获得时间区域相关信息，检查获取成功")
        timedate.getZoneInfo(self.zone)

    def tearDown(self):
        self.Step("收尾:无")
