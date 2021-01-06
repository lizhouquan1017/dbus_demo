# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          029_getCursorThumbnail
# @Test Description:      用于获取光标主题缩略图，返回String类型参数.
# @Test Condition:        无
# @Test Step:             1.调用Thumbnail函数，用于获取光标主题缩略图，返回String类型参数；
# @Test Result:           1.返回String类型参数;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import appearance
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.resource = 'cursor'
        self.resource_name = 'bloom-dark'

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于获取光标主题缩略图，返回String类型参数")
        appearance.getGtkThumbnail(self.resource, self.resource_name)

    def tearDown(self):
        self.Step("收尾:将光标主题恢复为默认格式bloom")
        appearance.reset()
