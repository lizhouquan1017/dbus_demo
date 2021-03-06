# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_listUserApps
# @Test Description:      获取支持特定mime的所有用户App信息的Json字符串.
# @Test Condition:        无
# @Test Step:             1.调用ListUserApps函数，获取支持特定mime的所有用户App信息的Json字符串；
# @Test Result:           1.支持特定mime类型的一系列用户App信息的Json格式字符串;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import mime
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.mimeType = "application/aac"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用ListUserApps函数，获取支持特定mime的所有用户App信息的Json字符串")
        mime.listUserApps(self.mimeType)

    def tearDown(self):
        self.Step("收尾:无")
