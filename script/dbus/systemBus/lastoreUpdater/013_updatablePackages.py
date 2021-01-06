# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          013_updatablePackages
# @Test Description:      读取可以更新的软件包列表
# @Test Condition:
# @Test Step:             1.读取 UpdatablePackages 属性
# @Test Result:           1.返回Arrayof[String]结构数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import updatablePackages


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("读取可以更新的软件包列表")
        assert updatablePackages()

    def tearDown(self):
        pass
