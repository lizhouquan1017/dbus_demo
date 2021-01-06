# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_deleteApp
# @Test Description:      删除APP对一系列mime的支持.
# @Test Condition:        无
# @Test Step:             1.调用DeleteApp函数，删除APP对一系列mime的支持；
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
        self.mimeType = "application/ogg"
        self.desktopId = "deepin-movie.desktop"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用DeleteApp函数，删除APP对一系列mime的支持")
        mime.deleteApp(self.mimeType, self.desktopId)

    def tearDown(self):
        self.Step("收尾:无")
