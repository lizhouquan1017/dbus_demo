# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          017_dockedApps
# @Test Description:      []string DockedApps:当前dock栏驻留的应用包名称列表
# @Test Condition:        1.无
# @Test Step:             1.读取属性 DockedApps
# @Test Result:           1.返回一个 []string 数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import dock


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取属性 DockedApps")
        dock.dockedApps()

    def tearDown(self):
        self.Step("收尾:无")        
    

