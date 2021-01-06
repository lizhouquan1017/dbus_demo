# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          010_jobEnd
# @Test Description:      JobEnd(string kind,bool success,string errMsg)
#                         在备份或恢复任务结束发出。
#                         参数
#                             kind 在备份时为 "backup"，在恢复时为 "restore"。
#                             success 是否成功
#                             errMsg 失败时的错误消
# @Test Condition:        1.无
# @Test Step:             1.使用dbus-monitor命令监控com.deepin.ABRecovery
#                         2.完成备份一次
#                         3.解析dbus-monitor结果,是否监控到 JobEnd 信号,判断'string "backup"'是否在返回值中
# @Test Result:           3.监控到 JobEnd 信号,'string "backup"'在返回值中
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time
import logging

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import abRecovery
from aw.dbus.dbus_common import start_monitor_signal_for_system, stop_monitor_signal


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")
        self.single = 'JobEnd'
        self.parse_flgs = 'string "backup"'

        self.Step("步骤1:使用dbus-monitor命令监控com.deepin.ABRecovery")
        self.dbus_monitor = start_monitor_signal_for_system(abRecovery.IFACE_NAME,
                                                            abRecovery.DBUS_PATH,
                                                            member=self.single)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤2:完成备份一次")
        abRecovery.start_backup()
        time.sleep(2)
        for item in range(1, 200):
            if abRecovery.backing_up():
                time.sleep(5)
                logging.info(f'备份未结束,第{item}圈')
                continue
            else:
                logging.info('备份结束')
                break

        self.Step("""步骤3:解析dbus-monitor结果,是否监控到 JobEnd 信号,判断'string "backup"'是否在返回值中""")
        abRecovery.jobEnd(self.dbus_monitor, self.parse_flgs)
        time.sleep(5)

    def tearDown(self):
        self.Step("收尾:stop_monitor_signal")
        stop_monitor_signal(self.dbus_monitor)
