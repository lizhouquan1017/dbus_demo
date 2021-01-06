# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          024_setScreenScaleFactors
# @Test Description:      用于设置每个屏幕的缩放比例，和GetScreenScaleFactors对应参数.
# @Test Condition:        无
# @Test Step:             1.调用SetScreenScaleFactors函数，用于设置每个屏幕的缩放比例，和GetScreenScaleFactors对应参数；
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
        self.scale_factor = appearance.checkScreenScaleFactors()

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于设置每个屏幕的缩放比例，和GetScreenScaleFactors对应参数")
        appearance.setScreenScaleFactors(self.scale_factor)

    def tearDown(self):
        self.Step("收尾:无")
