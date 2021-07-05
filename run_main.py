# 用例路径
import os
import time
import unittest
from BeautifulReport import BeautifulReport

# 用例路径
case_path = os.path.dirname(os.path.abspath(__file__)) + "/scripts"

# 定义测试套件
suite = unittest.defaultTestLoader.discover(case_path)

# 报告路径
report_path = os.path.dirname(os.path.abspath(__file__)) + "/report/web学生端接口自动化测试"

# 报告名称
# report_name = time.strftime("%Y_%m%d_%H:%M:%S")

BeautifulReport(suite).report(report_dir=report_path, description="web学生端接口自动化测试")
