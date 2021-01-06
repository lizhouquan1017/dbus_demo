# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_newSearchWithStrList
# @Test Description:      创建一个搜索数据集合，数据类型是字符串列表，列表的每个元素即是搜索的目标，也是搜索的关键字。.
# @Test Condition:        无
# @Test Step:             1.调用NewSearchWithStrList函数，创建一个搜索数据集合，数据类型是字符串列表；
# @Test Result:           1.md5sum: md5值，作为此搜索数据集合的标识符。ok: true 表示创建成功，否则失败。;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import daemonSearch
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.data = ["西瓜", "橘子"]

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用NewSearchWithStrList函数，创建一个搜索数据集合，数据类型是字符串列表")
        daemonSearch.newSearchWithStrList(self.data)

    def tearDown(self):
        self.Step("收尾:无")
