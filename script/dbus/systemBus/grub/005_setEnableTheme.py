# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_setEnableTheme
# @Test Description:      设置GRUB菜单中开启主题
# @Test Condition:
# @Test Step:             1.设置GRUB菜单中开启主题；
#
# @Test Result:           1.检查设置GRUB菜单中开启主题成功;
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
        self.passwd = self.get_data('passwd')
        grub.setEnableTheme(self.passwd, 'disable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置GRUB菜单中开启主题")
        grub.setEnableTheme(self.passwd, 'enable')

        self.CheckPoint("检查点1：检查开启主题成功")
        grub.checkThemeStatus('enable')

    def tearDown(self):
        self.Step("收尾:")
