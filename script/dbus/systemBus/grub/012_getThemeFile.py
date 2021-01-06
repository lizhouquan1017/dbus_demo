# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          012_getThemeFile
# @Test Description:      在开启了GRUB菜单主题后,使用的主题文件
# @Test Condition:
# @Test Step:             1.获取在开启了GRUB菜单主题后,使用的主题文件 ；
#
# @Test Result:           1.检查获取使用的主题文件成功;
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
        self.Step("步骤1:获取在开启了GRUB菜单主题后,使用的主题文件，并检查成功")
        grub.getThemeFile()

    def tearDown(self):
        self.Step("收尾:")
