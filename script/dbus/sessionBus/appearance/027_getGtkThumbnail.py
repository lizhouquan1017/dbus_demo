# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          027_getGtkThumbnail
# @Test Description:      用于获取gtk主题缩略图，返回String类型参数.
# @Test Condition:        无
# @Test Step:             1.调用Thumbnail函数，用于获取gtk主题缩略图，返回String类型参数；
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
        self.resource = 'gtk'
        self.resource_name = 'deepin'

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于获取gtk主题缩略图，返回String类型参数")
        appearance.getGtkThumbnail(self.resource, self.resource_name)

    def tearDown(self):
        self.Step("收尾:无")
