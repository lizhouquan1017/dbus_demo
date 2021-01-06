# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_getSinks
# @Test Description:      获取输出设备的dbus路径的集合信息
# @Test Condition:
# @Test Step:             1.获取输出设备的dbus路径的集合信息；
# @Test Result:           1.检查获取信息成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audio


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取输出设备的dbus路径的集合信息，检查获取信息成功")
        audio.getSinkInputs()

    def tearDown(self):
        self.Step("收尾:无")
