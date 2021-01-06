# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_deleteUserApp
# @Test Description:      删除对默认程序支持的App列表中的某个用户App.
# @Test Condition:        无
# @Test Step:             1.调用DeleteUserApp函数，删除对默认程序支持的App列表中的某个用户App；
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
        self.Step("步骤1：调用AddUserApp函数，添加用户App和用户App支持的一系列mime")
        mime.addUserApp(self.mimeType, self.desktopId)

        self.Step("步骤2：调用DeleteUserApp函数，删除对默认程序支持的App列表中的某个用户App")
        mime.deleteUserApp(self.desktopId)

    def tearDown(self):
        self.Step("收尾:无")
