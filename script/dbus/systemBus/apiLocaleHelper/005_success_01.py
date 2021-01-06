# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          005_success_01
# @Test Description:      Success(ok Boolean, reason String)
#                         设置成功信号
#                         ok：是否成功，true成功，false失败
#                         reason：失败原因，如果ok为true，返回空字符串
# @Test Condition:        无
# @Test Step:             1.使用dbus-monitor命令监控com.deepin.api.LocaleHelper
#                         2.调用 GenerateLocale 函数,传入正确的语言信息
#                         3.解析dbus-monitor结果,是否监控到 Success 信号,判断 'boolean true' 是否在返回值中
# @Test Result:           3.监控到 Success 信号,'boolean true' 在返回值中
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import apiLocaleHelper
from aw.dbus.dbus_common import start_monitor_signal_for_system, stop_monitor_signal


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")
        self.single = 'Success'
        self.parse_flgs = 'boolean true'
        self.passwd = self.get_data('passwd')

        self.Step("步骤1:使用dbus-monitor命令监控com.deepin.api.LocaleHelper")
        self.dbus_monitor = start_monitor_signal_for_system(apiLocaleHelper.IFACE_NAME,
                                                            apiLocaleHelper.DBUS_PATH,
                                                            member=self.single)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤2:调用 GenerateLocale 函数,传入正确的语言信息")
        apiLocaleHelper.generateLocale(passwd=self.passwd)
        time.sleep(5)

        self.Step("步骤3:解析dbus-monitor结果,是否监控到Success信号,判断'boolean true'是否在返回值中")
        apiLocaleHelper.success(self.dbus_monitor, self.parse_flgs)
        time.sleep(5)

    def tearDown(self):
        self.Step("收尾:stop_monitor_signal")
        stop_monitor_signal(self.dbus_monitor)
