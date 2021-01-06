# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          018_opacity
# @Test Description:      double Opacity:当前dock栏透明度，默认0.4
# @Test Condition:        1.无
# @Test Step:             1.读取属性 Opacity
# @Test Result:           1.返回一个 double 数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import dock


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取属性 Opacity")
        dock.opacity()

    def tearDown(self):
        self.Step("收尾:无")
