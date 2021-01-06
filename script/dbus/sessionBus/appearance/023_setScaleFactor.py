# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          023_setScaleFactor
# @Test Description:      用于设置窗体缩放比例.
# @Test Condition:        无
# @Test Step:             1.调用SetScaleFactor函数，用于设置窗体缩放比例；
# @Test Result:           1.检查执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import appearance
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.scale_factor = 1.0

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于设置窗体缩放比例")
        appearance.setScaleFactor(self.scale_factor)

    def tearDown(self):
        self.Step("收尾:无")
