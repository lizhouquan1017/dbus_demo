# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_getCheckIntervalAndTime
# @Test Description:      获取检查周期和最新的检查时间
# @Test Condition:
# @Test Step:             1.调用 GetCheckIntervalAndTime 函数,获取检查周期和最新的检查时间
# @Test Result:           1.获取到获取检查周期和最新的检查时间
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import getCheckIntervalAndTime


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        assert getCheckIntervalAndTime()

    def tearDown(self):
        pass
