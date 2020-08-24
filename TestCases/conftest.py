# -*- coding: utf-8 -*-

from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas.common_data import DoUrl
import pytest

driver = None


# 声明它是一个fixture
@pytest.fixture(scope='class')
def access_web():  # 访问web页面
    global driver
    # 前置操作
    print('========所有测试用例之前执行，只执行一次========')
    driver = webdriver.Chrome()
    driver.get(DoUrl.login_url)
    lp = LoginPage(driver)
    yield (driver, lp) # 分割线  后面接返回值g
    # 后置操作
    print('========所有测试用例之后执行，只执行一次========')
    driver.quit()


@pytest.fixture
def refresh_page():  # 刷新
    global driver
    # 前置操作
    yield
    # 后置操作
    driver.refresh()