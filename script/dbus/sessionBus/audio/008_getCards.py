# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_getCards
# @Test Description:      获取声卡信息
# @Test Condition:
# @Test Step:             1.获取声卡信息；
# @Test Result:           1.检查获取成功;
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
        self.Step("步骤1:获取降噪开关状态，并检查获取成功")
        audio.getCards()

    def tearDown(self):
        self.Step("收尾:无")
