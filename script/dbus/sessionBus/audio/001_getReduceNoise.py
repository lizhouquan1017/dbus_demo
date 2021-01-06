# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_getReduceNoise
# @Test Description:      获取降噪开关状态
# @Test Condition:
# @Test Step:             1.获取降噪开关状态；
# @Test Result:           1.检查输出值为布尔值,则表示获取状态成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import audio


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.sp3
    def test_step(self):
        self.Step("步骤1:获取降噪开关状态，并检查获取成功")
        audio.getReduceNoise()

    def tearDown(self):
        self.Step("收尾:无")
