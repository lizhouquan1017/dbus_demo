# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          014_getBackground
# @Test Description:      用于获取GRUB引导菜单的背景文件的绝对路径
# @Test Condition:
# @Test Step:             1.用于获取GRUB引导菜单的背景文件的绝对路径；
#
# @Test Result:           1.检查获取背景文件的绝对路径成功;
#
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import grub


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.passwd = self.get_data('passwd')

        self.Step("预制条件2:设置GRUB菜单中开启主题")
        grub.setEnableTheme(self.passwd, 'enable')
        time.sleep(5)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于获取GRUB引导菜单的背景文件的绝对路径，并检查成功")
        grub.getBackground()

    def tearDown(self):
        self.Step("收尾:")
