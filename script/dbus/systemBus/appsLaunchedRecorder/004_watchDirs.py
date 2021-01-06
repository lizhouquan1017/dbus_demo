# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          004_watchDirs
# @Test Description:      WatchDirs(string[] dirs)
#                         增加监视的目录，监视该目录文件的删除和新增事件
#                         参数
#                             dirs: 要增加的被监视目录列表
#                         返回
#                             无
# @Test Condition:        1.创建一个测试用目录
# @Test Step:             1.调用 WatchDirs 函数,增加监视的目录，监视该目录文件的删除和新增事件
# @Test Result:           1.调用成功无报错
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import shutil
import os
import random

import pytest

from frame import constant
from frame.base import OSBase
from aw.dbus.systemBus import appsLaunchedRecorder


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:创建一个测试用目录")
        dir_name = f'WatchDirs{random.randint(0, 100)}'
        self.dir_path = os.path.join(constant.resoure_path, dir_name)
        if os.path.exists(self.dir_path):
            shutil.rmtree(self.dir_path)
            os.mkdir(self.dir_path)
        else:
            os.mkdir(self.dir_path)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 WatchDirs 函数,增加监视的目录，监视该目录文件的删除和新增事件")
        appsLaunchedRecorder.watchDirs(self.dir_path)

    def tearDown(self):
        self.Step("收尾:删除测试目录")
        shutil.rmtree(self.dir_path)
