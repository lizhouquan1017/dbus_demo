# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          007_Version
# @Test Description:      String Version (read)
#                         当前系统版本, 例如: "2015 Desktop"
# @Test Condition:        1.无
# @Test Step:             1.调用接口读取 Version 属性值
# @Test Result:           1.返回 String 类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************
import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import daemonSystemInfo


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用接口读取 Version 属性值")
        daemonSystemInfo.version()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(1)
