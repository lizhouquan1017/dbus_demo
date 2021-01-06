# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_getWallpaperSlideShow
# @Test Description:      用于根据显示器名称获取该显示器壁纸切换间隔.
# @Test Condition:        无
# @Test Step:             1.调用GetWallpaperSlideShow函数，获取当前显示器下壁纸切换间隔；
# @Test Result:           1.返回string类型数据;
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

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用GetWallpaperSlideShow函数，获取当前显示器下壁纸切换间隔")
        appearance.getWallpaperSlideShow(self.name)

    def tearDown(self):
        self.Step("收尾:无")
