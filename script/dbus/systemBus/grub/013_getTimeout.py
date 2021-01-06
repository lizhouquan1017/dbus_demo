# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          013_getTimeout
# @Test Description:      用户无操作时,在GRUB菜单界面的停留时间
# @Test Condition:
# @Test Step:             1.获取用户无操作时,在GRUB菜单界面的停留时间；
#
# @Test Result:           1.检查获取停留时间成功;
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
        self.Step("步骤1:获取用户无操作时,在GRUB菜单界面的停留时，并检查成功")
        grub.timeOut()

    def tearDown(self):
        self.Step("收尾:")
