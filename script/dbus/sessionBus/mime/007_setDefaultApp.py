# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_setDefaultApp
# @Test Description:      为一系列mime设置同一个默认的App.
# @Test Condition:        无
# @Test Step:             1.调用SetDefaultApp函数，为一系列mime设置同一个默认的App；
# @Test Result:           1.检查接口执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import mime
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.mimeTypes = ["application/aac", "application/musepack"]
        self.desktopId = "deepin-music.desktop"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用SetDefaultApp函数，为一系列mime设置同一个默认的App")
        mime.setDefaultApp(self.mimeTypes, self.desktopId)

    def tearDown(self):
        self.Step("收尾:无")
