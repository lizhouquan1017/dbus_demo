# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          021_sourceSetPort
# @Test Description:      设置此设备的当前使用端口
# @Test Condition:
# @Test Step:             1.设置此设备的当前使用端口；
# @Test Result:           1.检查设置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audioSource


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")
        self.name = '12'

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置此设备的当前使用端口，检查设置成功")
        audioSource.sourceSetPort(self.name)

    def tearDown(self):
        self.Step("收尾:无")
