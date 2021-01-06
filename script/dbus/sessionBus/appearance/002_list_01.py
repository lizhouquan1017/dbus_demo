# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_list_01
# @Test Description:      用于列出gtk类型下的文件和资源，并返回json格式列表.
# @Test Condition:        无
# @Test Step:             1.调用List函数，获取当前gtk类型下的文件和资源列表；
# @Test Result:           1.返回string[] list类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import appearance
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.resource = "gtk"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用List函数，获取当前gtk类型下的文件和资源列表")
        appearance.getList(self.resource)

    def tearDown(self):
        self.Step("收尾:无")
