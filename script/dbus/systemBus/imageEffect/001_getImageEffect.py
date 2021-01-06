# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_getImageEffect
# @Test Description:      将图片根据需求特效,生成图片
# @Test Condition:
# @Test Step:             1.将图片根据需求特效,生成图片；
# @Test Result:           1.检查生成图片成功;
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
        self.Step("步骤1:将图片根据需求特效,生成图片,并检查成功")
        imageEffect.getImageEffect(self.effect, self.imagefile)

    def tearDown(self):
        self.Step("收尾:")
        imageEffect.delete(self.effect, self.imagefile)
