# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_searchString
# @Test Description:      进行数据集合的搜索，支持模糊拼音搜索。.
# @Test Condition:        无
# @Test Step:             1.调用SearchString函数，进行数据集合的搜索，支持模糊拼音搜索。；
# @Test Result:           1.result: 匹配的结果;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import daemonSearch
from aw.dbus.sessionBus.daemonSearch import getSearchWithStrList
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.word = ["西瓜"]
        self.md5sum = getSearchWithStrList(self.word)[0]
        self.strs = ["xi", "gua"]

    @pytest.mark.public
    def test_step(self):
        for str_word in self.strs:
            self.Step("步骤1：调用SearchString函数，进行数据集合的搜索，支持模糊拼音搜索。")
            daemonSearch.searchString(str_word, self.md5sum)

    def tearDown(self):
        self.Step("收尾:无")
