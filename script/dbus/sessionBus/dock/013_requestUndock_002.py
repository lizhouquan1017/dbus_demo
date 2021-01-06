# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          013_requestUndock_002
# @Test Description:      RequestUndock(string desktopFile) -> (bool ok),取消驻留在dock上的应用的desktop文件路径参数
#                         desktopFile: 应用的desktop文件路径
#                         ok: 取消成功为true，否则失败
# @Test Condition:        1.dde-file-manager.desktop 未固定在dock上
# @Test Step:             1.调用 RequestUndock 函数,请求应用的desktop文件路径取消驻留在dock上
# @Test Result:           1.返回 bool 类型数据,返回的数据为False
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

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 RequestUndock 函数,请求应用的desktop文件路径取消驻留在dock上")
        result, state = dock.requestUndock()
        self.CheckPoint("检查点1:返回 bool 类型数据,返回的数据为False")
        assert state is 0
        assert result is False

    def tearDown(self):
        self.Step("收尾:无")
        dock.set_app_docked()
        time.sleep(2)
