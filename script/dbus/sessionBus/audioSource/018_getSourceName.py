# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          018_getSourceName
# @Test Description:      设备名
# @Test Condition:
# @Test Step:             1.读取Name属性值；
# @Test Result:           1.检查读取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audioSource


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取Name属性值，检查读取成功")
        audioSource.getSourceName()

    def tearDown(self):
        self.Step("收尾:无")
