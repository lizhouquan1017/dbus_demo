# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          003_setLocale_01
# @Test Description:      SetLocale (String locale) ↦ ()
#                         按照语言设置默认的本地语言
#                         参数
#                             locale：需要设置的本地语言的语言类型字符串(语言字符串文件可参照：/etc/locale.gen)
#                         返回
#                             无
#                         报错
#                             invalid locale：locale传入错误将报此错
# @Test Condition:        1.无
# @Test Step:             1.调用 SetLocale 函数,传入正确的语言信息
# @Test Result:           1.调用正常无报错
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
        self.Step("步骤1:调用 SetLocale 函数,传入正确的语言信息")
        apiLocaleHelper.setLocale(passwd=self.passwd)

    def tearDown(self):
        self.Step("收尾:无")
