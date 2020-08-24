# -*- coding: utf-8 -*-

import unittest
from Common.congfig_path import *



# 实例化套件对象
suite = unittest.TestSuite()

# TestLoader用法
# 1、实例化TestLoader对象
# 2、使用discover去找到一个目录下所有的测试用例
# 3、使用suite
loader = unittest.TestLoader()
suite.addTest(loader.discover(test_case_path))

# 运行
with open(report_path, 'w+', encoding='utf-8') as file:
    runner = unittest.TextTestRunner(stream=file, verbosity=2)
    runner.run(suite)