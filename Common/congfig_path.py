
import os

project_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 截图路径
screenshot_path = os.path.join(project_path, r'Output\screenshots')
# 日志路径
log_path = os.path.join(project_path, r'Output\logs')
# 报告路径
report_path = os.path.join(project_path, r'Output\reports\autoTest_report.html')
# 测试用例路径
test_case_path = os.path.join(project_path, 'TestCases')
# 测试数据路径
test_data_path = os.path.join(project_path, 'TestDatas')
