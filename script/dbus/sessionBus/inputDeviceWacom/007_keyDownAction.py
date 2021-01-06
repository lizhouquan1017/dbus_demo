# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          007_keyDownAction
# @Test Description:      string KeyDownAction (readwrite)
#                         下键触发的动作
# @Test Condition:        无
# @Test Step:             1.读取 KeyDownAction 属性值
# @Test Result:           1.返回 string 类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceWacom


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取 KeyDownAction 属性值")
        assert inputDeviceWacom.keyDownAction()

    def tearDown(self):
        pass
