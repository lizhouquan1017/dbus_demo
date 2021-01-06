# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_sourceGetMeter
# @Test Description:      返回Meter对象的path
# @Test Condition:
# @Test Step:             1.返回Meter对象的path；
# @Test Result:           1.检查返回成功;
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
        self.Step("步骤1:返回Meter对象的path，并检查获取成功")
        audioSource.sourceGetMeter()

    def tearDown(self):
        self.Step("收尾:无")
