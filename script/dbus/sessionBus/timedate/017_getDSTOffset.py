# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          017_getDSTOffset
# @Test Description:      夏令时偏移量
# @Test Condition:
# @Test Step:             1.获取夏令时偏移量值；
# @Test Result:           1.检查获取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取夏令时偏移量值，并检查获取成功")
        timedate.getDSTOffset()

    def tearDown(self):
        pass
