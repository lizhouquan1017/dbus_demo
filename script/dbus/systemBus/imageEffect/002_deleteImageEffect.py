# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_deleteImageEffect
# @Test Description:      根据效果和图片名,删除生成的文件
# @Test Condition:
# @Test Step:             1.根据效果和图片名,删除生成的文件；
# @Test Result:           1.检查删除生成的文件成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import imageEffect


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.effect = self.get_data('effect')
        self.imagefile = self.get_data('imagefile')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:根据效果和图片名,删除生成的文件,检查删除成功")
        imageEffect.delete(self.effect, self.imagefile)

    def tearDown(self):
        self.Step("收尾:")
