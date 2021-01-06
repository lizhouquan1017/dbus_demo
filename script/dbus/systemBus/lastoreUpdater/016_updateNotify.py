# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          016_updateNotify
# @Test Description:      是否使能通知更新标志
# @Test Condition:
# @Test Step:             1.读取 UpdateNotify 属性
# @Test Result:           1.返回Boolean类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import updateNotify


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("读取是否使能通知更新标志")
        assert updateNotify()

    def tearDown(self):
        pass
