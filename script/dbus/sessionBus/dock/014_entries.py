# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          014_entries
# @Test Description:      objectPath[] Entries (read)
#                         在com.deepin.dde.daemon.Dock服务下，针对每个打开的应用并且在dock上有相应icon显示，dock模块会生成一个
#                         entires并关联一个接口/com/deepin/dde/daemon/Dock/entries/xx，Entries存储的就是所有的关联接口列表
# @Test Condition:        1.无
# @Test Step:             1.读取属性 Entries
# @Test Result:           1.返回一个dbus.Array数据,各成员为dbus.String数据
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
        self.Step("步骤1:读取属性 Entries")
        dock.entries()

    def tearDown(self):
        self.Step("收尾:无")
