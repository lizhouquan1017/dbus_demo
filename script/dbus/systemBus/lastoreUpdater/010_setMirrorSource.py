# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          010_setMirrorSource
# @Test Description:      将id添加到用于下载软件的镜像源
# @Test Condition:        为默认源
# @Test Step:             1.设置源为默认源
#                         2.修改为Aliyun源
#                         3.修改为Kernel源
#                         4.修改为为默认源
# @Test Result:           2.修改源为Aliyun源,成功
#                         3.修改源为Kernel源,成功
# @Test Remark:           如果添加失败，则会恢复之前的镜像源
# @Author:  ut001627
# ***************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus.lastoreUpdater import setMirrorSource


class TestCase(OSBase):

    def setUp(self):
        self.passwd = self.get_data('passwd')
        setMirrorSource(self.passwd, 'default')

    @pytest.mark.public
    def test_step(self):
        assert setMirrorSource(self.passwd, 'Aliyun', 'Kernel')

    def tearDown(self):
        pass
