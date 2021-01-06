# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_isDiskSpaceSufficient
# @Test Description:      判断磁盘是否有剩余的空间.
# @Test Condition:        无
# @Test Step:             1.调用IsDiskSpaceSufficient函数，判断磁盘是否有剩余的空间；
# @Test Result:           1.result: true 如果剩余空间大于10MiB，false 则代表剩余空间不足;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import lastoreSessionHelper
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用IsDiskSpaceSufficient函数，判断磁盘是否有剩余的空间")
        lastoreSessionHelper.isDiskSpaceSufficient()

    def tearDown(self):
        self.Step("收尾:无")
