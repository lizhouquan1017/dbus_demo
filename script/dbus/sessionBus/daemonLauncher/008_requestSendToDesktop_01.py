# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          008_requestSendToDesktop_01
# @Test Description:      请求将指定id的程序创建桌面图标,执行结果，true表示成功，id已经有桌面图标则报错
# @Test Condition:        桌面图标不存在桌面
# @Test Step:             1.删除桌面图标
#                         2.调用RequestSendToDesktop接口,请求将指定id的程序创建桌面图标
# @Test Result:           2.返回true
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import requestSendToDesktop, requestRemoveFromDesktop


class TestCase(OSBase):

    def setUp(self):
        self.app_id = 'dde-file-manager'
        self.Step(f'步骤1:删除{self.app_id}桌面图标')
        requestRemoveFromDesktop(app_id=self.app_id, ignore=True)
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step(f'步骤2:创建{self.app_id}桌面图标')
        assert requestSendToDesktop(app_id=self.app_id, is_exists=False, is_clear=False)
        time.sleep(2)

    def tearDown(self):
        pass
