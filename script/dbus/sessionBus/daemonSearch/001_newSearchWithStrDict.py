# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_newSearchWithStrDict
# @Test Description:      通过字符字典进行搜索创建一个搜索数据集合，数据类型是 map[string]string, map 的键是要搜索的目标，值是搜索关键字。.
# @Test Condition:        无
# @Test Step:             1.调用NewSearchWithStrDict函数，通过字符字典进行搜索 创建一个搜索数据集合；
# @Test Result:           1.md5sum: md5值，作为此搜索数据集合的标识符。ok: true 表示创建成功，否则失败;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import daemonSearch
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.map = {"target1": "西瓜", "target2": "橘子"}

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用NewSearchWithStrDict函数，通过字符字典进行搜索 创建一个搜索数据集合")
        daemonSearch.newSearchWithStrDict(self.map)

    def tearDown(self):
        self.Step("收尾:无")
