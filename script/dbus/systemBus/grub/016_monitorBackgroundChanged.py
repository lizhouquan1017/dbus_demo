# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          016_monitorBackgroundChanged
# @Test Description:      GRUB引导菜单背景修改时触发该信号
# @Test Condition:
# @Test Step:             1.GRUB引导菜单背景修改时触发该信号；
#
# @Test Result:           1.检查信号接收成功;
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
        self.filename1 = self.get_data('filename1')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:监控GRUB引导菜单背景修改时触发该信号，并检查接收信号成功")
        grub.backGroundChanged(self.passwd, self.filename1)

    def tearDown(self):
        self.Step("收尾:")
