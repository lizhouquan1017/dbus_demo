# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          017_actionInfos
# @Test Description:      InfoStruct[] ActionInfos (read)
#                         type InfoStruct struct {
#                            string Action
#                            string Desc
#                         }
#                         信息列表
#                         字段含义:
#                                 Action : 响应
#                                 Desc : 描述说明
# @Test Condition:        无
# @Test Step:             1.读取 ActionInfos 属性值
# @Test Result:           1.返回 InfoStruct[] 类型数据
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceWacom


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取 ActionInfos 属性值")
        assert inputDeviceWacom.actionInfos()

    def tearDown(self):
        self.Step("收尾:无")
