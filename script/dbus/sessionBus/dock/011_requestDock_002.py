# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          010_requestDock
# @Test Description:      RequestDock(string desktopFile, int32 index) -> (bool ok),请求应用的desktop文件路径驻留在dock上
#                         desktopFile: 应用的desktop文件路径
#                         index: 驻留在dock上的应用位置索引，从左往右从0开始
#                         ok: 发送成功为true，否则失败
# @Test Condition:        1.dde-file-manager.desktop 未固定在dock上
# @Test Step:             1.调用 RequestDock 函数,请求应用的desktop文件路径驻留在dock上
# @Test Result:           1.返回 bool 类型数据,返回的数据为True
# @Test Remark:
# @Author:  ut001627
# ***************************************************
import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import dock


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:dde-file-manager.desktop 未固定在dock上")
        dock.set_app_docked(target=False)
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 RequestDock 函数,请求应用的desktop文件路径驻留在dock上")
        result, state = dock.requestDock()
        self.CheckPoint("检查点1:返回 bool 类型数据,返回的数据为True")
        assert state is 0
        assert result is True

    def tearDown(self):
        self.Step("收尾:无")
        dock.set_app_docked()
        time.sleep(2)
