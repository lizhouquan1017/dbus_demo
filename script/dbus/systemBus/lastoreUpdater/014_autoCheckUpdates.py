# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          014_autoCheckUpdates
# @Test Description:      是否使能自动检查更新标志
# @Test Condition:
# @Test Step:             1.读取 AutoCheckUpdates 属性
# @Test Result:           1.返回Boolean类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import autoCheckUpdates


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("读取是否使能自动检查更新标志")
        assert autoCheckUpdates()

    def tearDown(self):
        pass
