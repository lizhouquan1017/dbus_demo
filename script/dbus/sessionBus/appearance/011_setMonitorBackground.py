# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          011_setMonitorBackground
# @Test Description:      用于根据显示器名称设置桌面背景参数.
# @Test Condition:
# @Test Step:             1.调用SetMonitorBackground函数，获取当前显示器下壁纸切换间隔；
# @Test Result:           1.检测接口执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import appearance
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.name = "HDMI-2"
        self.imagefile = self.get_data('desktop_imagefile')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调SetMonitorBackground函数，设置桌面背景参数")
        appearance.setMonitorBackground(self.name, self.imagefile)

    def tearDown(self):
        self.Step("收尾:无")
