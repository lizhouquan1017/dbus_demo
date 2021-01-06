# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          011_getUpdating
# @Test Description:      当前是否处于系统更新状态
# @Test Condition:
# @Test Step:             1.获取当前是否处于系统更新状态 ；
#
# @Test Result:           1.检查当前是否处于系统更新状态成功;
#
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import grub


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取当前是否处于系统更新状态检查状态成功")
        grub.getUpdating()

    def tearDown(self):
        self.Step("收尾:")
