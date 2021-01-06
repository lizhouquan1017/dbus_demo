# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          009_requestSendToDesktop_02
# @Test Description:      请求将指定id的程序创建桌面图标
# @Test Condition:        桌面图标存在桌面
# @Test Step:             1.创建桌面图标
#                         2.调用RequestSendToDesktop接口,请求将指定id的程序创建桌面图标
# @Test Result:           2.报错
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
        self.Step(f'步骤1:创建{self.app_id}桌面图标')
        requestSendToDesktop(app_id=self.app_id, ignore=True)
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step('步骤2:调用接口')
        assert requestSendToDesktop(app_id=self.app_id, is_exists=True, is_clear=False)
        time.sleep(2)

    def tearDown(self):
        requestRemoveFromDesktop(app_id=self.app_id, ignore=True)
        time.sleep(1)
