# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_getEnableTheme
# @Test Description:      获取是否开启了GRUB菜单主题
# @Test Condition:
# @Test Step:             1.获取是否开启了GRUB菜单主题 ；
#
# @Test Result:           1.检查获取是否开启了GRUB菜单主题成功;
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
        self.Step("步骤1:获取是否开启了GRUB菜单主题检查状态成功")
        grub.getEnableTheme()

    def tearDown(self):
        self.Step("收尾:")
