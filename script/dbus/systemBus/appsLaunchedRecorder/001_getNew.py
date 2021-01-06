# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_getNew
# @Test Description:      GetNew() -> (map[string][]string newApps),获取已经安装但从未打开使用过的应用列表
#                         newApps: 返回的map结构中,key表示应用的desktopFile所在目录,value表示从未打开的应用的id列表
# @Test Condition:        1.无
# @Test Step:             1.调用 GetNew 函数,获取已经安装但从未打开使用过的应用列表
# @Test Result:           1.返回 map[string][]string 类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import appsLaunchedRecorder


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 GetNew 函数,获取已经安装但从未打开使用过的应用列表")
        appsLaunchedRecorder.getNew()

    def tearDown(self):
        self.Step("收尾:无")
