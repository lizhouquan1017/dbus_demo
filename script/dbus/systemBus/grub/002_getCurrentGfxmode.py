# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_getCurrentGfxmode
# @Test Description:      获取当前GRUB引导菜单显示的分辨率
# @Test Condition:
# @Test Step:             1.当前GRUB引导菜单显示的分辨率；
#
# @Test Result:           1.检查当前GRUB引导菜单显示的分辨率成功;
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
        self.Step("步骤1:获取当前GRUB引导菜单显示的分辨率并检查成功")
        grub.gfxmode()

    def tearDown(self):
        self.Step("收尾:")
