# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_appearanceReset
# @Test Description:      用于重置个性化设置为默认设置参数.
# @Test Condition:        无
# @Test Step:             1.调用Reset函数，用于重置个性化设置为默认设置参数；
# @Test Result:           1.检查执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import appearance
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于重置个性化设置为默认设置参数")
        appearance.reset()

    def tearDown(self):
        self.Step("收尾:无")
