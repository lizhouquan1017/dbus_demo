# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          010_exist
# @Test Description:      bool Exist (read)
#                         是否存在
# @Test Condition:        无
# @Test Step:             1.读取 Exist 属性值
# @Test Result:           1.返回 bool 类型数据
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
        self.Step("步骤1:读取 Exist 属性值")
        assert inputDeviceWacom.exist()

    def tearDown(self):
        pass
