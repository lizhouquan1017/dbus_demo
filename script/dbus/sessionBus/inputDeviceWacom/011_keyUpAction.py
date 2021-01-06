# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          011_keyUpAction
# @Test Description:      string KeyUpAction (readwrite)
#                         上键触发的动作
# @Test Condition:        无
# @Test Step:             1.读取 KeyUpAction 属性值
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
        self.Step("步骤1:读取 KeyUpAction 属性值")
        assert inputDeviceWacom.keyUpAction()

    def tearDown(self):
        self.Step("收尾:无")        
    

