# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_generateLocale_02
# @Test Description:      GenerateLocale (String locale) ↦ ()
#                         按照传入的语言信息生成区域语言
#                         参数
#                             locale：需要生成的区域语言的语言类型字符串(语言字符串可参照：/etc/locale.gen)
#                         返回
#                             无
#                         报错
#                             invalid locale：locale传入错误将报此错
# @Test Condition:        1.无
# @Test Step:             1.调用 GenerateLocale 函数,传入错误的语言信息
# @Test Result:           1.引发invalid locale错误
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import apiLocaleHelper


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")
        self.passwd = self.get_data('passwd')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 GenerateLocale 函数,传入错误的语言信息")
        apiLocaleHelper.generateLocale(locale='test', target='error', passwd=self.passwd)

    def tearDown(self):
        self.Step("收尾:无")
