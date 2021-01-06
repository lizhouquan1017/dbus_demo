# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          017_fullscreen
# @Test Description:      开始菜单是否全屏显示：true-全屏显示、false-菜单显示
# @Test Condition:        无
# @Test Step:             1.读取属性Fullscreen
# @Test Result:           1.返回bool数据类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import fullscreen


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step('step01:读取属性Fullscreen')
        assert fullscreen()

    def tearDown(self):
        pass
