# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          007_setTimeout
# @Test Description:      用于设置用户无操作时,在GRUB菜单界面的停留时间
# @Test Condition:
# @Test Step:             1.设置用户无操作时,在GRUB菜单界面的停留时间；
#
# @Test Result:           1.检查设置成功;
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
        self.time_out = self.get_data('time_out')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:设置用户无操作时,在GRUB菜单界面的停留时间")
        grub.setTimeout(self.passwd, self.time_out)

        self.CheckPoint("检查点1：检查关闭主题成功")
        grub.checkSetTimeout(self.time_out)

    def tearDown(self):
        self.Step("收尾:")
