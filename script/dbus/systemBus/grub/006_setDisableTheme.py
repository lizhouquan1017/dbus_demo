# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_setDisableTheme.py
# @Test Description:      设置GRUB菜单中关闭主题
# @Test Condition:
# @Test Step:             1.设置GRUB菜单中关闭主题；
#
# @Test Result:           1.检查设置GRUB菜单中关闭主题成功;
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
        grub.setEnableTheme(self.passwd, 'enable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置GRUB菜单中关闭主题")
        grub.setEnableTheme(self.passwd, 'disable')

        self.CheckPoint("检查点1：检查关闭主题成功")
        grub.checkThemeStatus('disable')

    def tearDown(self):
        self.Step("收尾:")
        grub.setEnableTheme(self.passwd, 'enable')
