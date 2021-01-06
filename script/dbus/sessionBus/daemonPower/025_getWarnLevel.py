# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          025_getWarnLevel
# @Test Description:      低电量警告级别。
#                         0: None 无
#                         1: Low 低
#                         2: Danger 危险
#                         3: Critical 严重
#                         4: Action 行动
# @Test Condition:
# @Test Step:             1.读取WarnLevel属性值；
# @Test Result:           1.检查读取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import daemonPower


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取WarnLevel属性值，检查读取成功")
        daemonPower.getWarnLevel()

    def tearDown(self):
        self.Step("收尾:无")
