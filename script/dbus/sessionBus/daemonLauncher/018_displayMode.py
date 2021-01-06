# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          018_displayMode
# @Test Description:      开始菜单里面图标的显示模式：0-全部显示、1-分类显示，全屏模式时生效。
# @Test Condition:        无
# @Test Step:             1.读取属性DisplayMode
# @Test Result:           1.返回一个int32的数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus.daemonLauncher import displayMode


class TestCase(OSBase):

    def setUp(self):
        pass

    @pytest.mark.public
    def test_step(self):
        self.Step('步骤1:读取属性Fullscreen')
        assert displayMode()

    def tearDown(self):
        pass
