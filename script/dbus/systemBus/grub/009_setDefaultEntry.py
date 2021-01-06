# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_setDefaultEntry
# @Test Description:      用于设置GRUB引导菜单的默认入口
# @Test Condition:
# @Test Step:             1.用于设置GRUB引导菜单的默认入口；
#
# @Test Result:           1.检查设置GRUB引导菜单的默认入口成功;
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

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置GRUB引导菜单的默认入口")
        grub.setDefaultEntry(self.passwd, 'end_entry')

        self.CheckPoint("检查点1：检查设置GRUB引导菜单的默认入口成功")
        grub.checkSetDefaultEntry('end_entry')

    def tearDown(self):
        self.Step("收尾:")
        grub.setDefaultEntry(self.passwd, 'first_entry')
        grub.checkSetDefaultEntry('first_entry')
