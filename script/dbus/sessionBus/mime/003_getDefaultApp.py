# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_getDefaultApp
# @Test Description:      获取特定mime的默认App.
# @Test Condition:        无
# @Test Step:             1.调用GetDefaultApp函数，获取特定mime的默认App；
# @Test Result:           1.特定mime的默认程序App信息的Json格式字符串;
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
        self.Step("步骤1：调用GetDefaultApp函数，获取特定mime的默认App")
        mime.getDefaultApp(self.mimeType)

    def tearDown(self):
        self.Step("收尾:无")
