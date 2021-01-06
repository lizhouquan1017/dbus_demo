# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          004_clearLayoutOption
# @Test Description:      ClearLayoutOption() -> (),清空键盘布局选项
# @Test Condition:        1.无
# @Test Step:             1.调用 ClearLayoutOption 清空键盘布局选项,并检查是否清除成功
# @Test Result:           1.清除成功
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceKeyboard


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:清除所有option,并检查是否清除成功")
        inputDeviceKeyboard.clearLayoutOption()
        time.sleep(2)

    def tearDown(self):
        self.Step("收尾:无")
