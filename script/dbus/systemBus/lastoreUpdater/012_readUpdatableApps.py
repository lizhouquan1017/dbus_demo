# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          012_readUpdatableApps
# @Test Description:      读取当前可升级应用列表
# @Test Condition:
# @Test Step:             1.读取 UpdatableApps 属性
# @Test Result:           1.返回Arrayof[String]结构数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import updatableApps


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step('读取当前可升级应用列表')
        assert updatableApps()

    def tearDown(self):
        pass
