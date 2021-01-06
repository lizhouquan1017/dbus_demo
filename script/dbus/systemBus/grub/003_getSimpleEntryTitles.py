# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_getSimpleEntryTitles
# @Test Description:      用于获取GRUB引导菜单显示的标题
# @Test Condition:
# @Test Step:             1.用于获取GRUB引导菜单显示的标题；
#
# @Test Result:           1.检查获取GRUB引导菜单显示的标题成功;
#
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import grub


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:")
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:获取GRUB引导菜单显示的标题并检查成功")
        grub.getSimpleEntryTitles()

    def tearDown(self):
        self.Step("收尾:")
