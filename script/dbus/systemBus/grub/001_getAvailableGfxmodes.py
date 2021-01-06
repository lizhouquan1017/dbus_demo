# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_getAvailableGfxmodes
# @Test Description:      获取所有GRUB引导菜单可显示的图像输出分辨率
# @Test Condition:
# @Test Step:             1.用于获取所有GRUB引导菜单可显示的图像输出分辨率；
#
# @Test Result:           1.检查用于获取所有GRUB引导菜单可显示的图像输出分辨率成功;
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
        self.Step("步骤1:获取所有GRUB引导菜单可显示的图像输出分辨率且检查成功")
        grub.getAvailableGfxmodes()

    def tearDown(self):
        self.Step("收尾:")
