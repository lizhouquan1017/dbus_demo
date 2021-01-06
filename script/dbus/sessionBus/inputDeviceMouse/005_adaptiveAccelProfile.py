# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          005_adaptiveAccelProfile
# @Test Description:      bool AdaptiveAccelProfile (readwrite)  是否使用自适应加速配置
# @Test Condition:        1.无
# @Test Step:             1.调用接口读取 AdaptiveAccelProfile 属性值
# @Test Result:           1.返回 bool 数据类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceMouse


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用接口读取 AdaptiveAccelProfile 属性值")
        inputDeviceMouse.adaptiveAccelProfile()

    def tearDown(self):
        self.Step("收尾:无")        
    

