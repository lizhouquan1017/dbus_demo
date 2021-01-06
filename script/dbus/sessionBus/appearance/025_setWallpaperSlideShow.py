# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          025_setWallpaperSlideShow
# @Test Description:      用于根据屏幕名称设置该屏幕桌面壁纸的轮换时间参数.
# @Test Condition:        无
# @Test Step:             1.调用SetWallpaperSlideShow函数，用于根据屏幕名称设置该屏幕桌面壁纸的轮换时间参数；
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
        self.monitor_name = appearance.getMonitorName()
        self.slide_time = '60'

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于根据屏幕名称设置该屏幕桌面壁纸的轮换时间参数")
        appearance.setWallpaperSlideShow(self.monitor_name, self.slide_time)

    def tearDown(self):
        self.Step("收尾:无")
