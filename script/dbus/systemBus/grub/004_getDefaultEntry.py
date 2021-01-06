# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_getDefaultEntry
# @Test Description:      GRUB引导菜单默认的启动项
# @Test Condition:
# @Test Step:             1.获取GRUB引导菜单默认的启动项；
#
# @Test Result:           1.检查获取GRUB引导菜单默认的启动项成功;
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
        self.Step("步骤1:获取GRUB引导菜单默认的启动项并检查成功")
        grub.getDefaultEntry()

    def tearDown(self):
        self.Step("收尾:")
