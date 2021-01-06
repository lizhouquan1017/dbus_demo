# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          026_showDetail
# @Test Description:      用于显示特殊类型的详细信息，返回json格式列表参数.
# @Test Condition:        无
# @Test Step:             1.调用Show函数，用于显示特殊类型的详细信息，返回json格式列表参数；
# @Test Result:           1.返回json格式列表参数;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import appearance
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.resource_name = 'cursor'
        self.name_list = ['bloom']

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:用于根据屏幕名称设置该屏幕桌面壁纸的轮换时间参数")
        appearance.showDetail(self.resource_name, self.name_list)

    def tearDown(self):
        self.Step("收尾:无")
