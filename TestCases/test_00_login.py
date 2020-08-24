# -*- coding: utf-8 -*-

from PageObjects.index_page import IndexPage
from TestDatas.login_data import LoginData
import logging
import pytest


@pytest.mark.usefixtures("access_web")  # 在运行的时候，会去运行access_web函数
@pytest.mark.usefixtures("refresh_page")
class TestLogin:

    # 用户名或密码为空
    @pytest.mark.parametrize('item', LoginData.error_msg_from_login_box_data)
    def test_login_a_null_username_pwd(self, item,access_web):
        logging.info('===用户名或密码为空登录===')
        # 步骤 ddt
        access_web[1].login(item['username'], item['pwd'])
        # 断言
        assert (access_web[1].error_msg_from_login_box(), item['excepted'])

    # 密码错误
    def test_login_b_wrong_pwd(self, access_web):
        access_web[1].login(LoginData.error_msg_from_wrong_pwd_data['username'], LoginData.error_msg_from_wrong_pwd_data['pwd'])
        # 断言
        assert (access_web[1].error_msg_from_wrong_pwd(), LoginData.error_msg_from_wrong_pwd_data['excepted'])

    # 用户名错误
    def test_login_c_wrong_username(self, access_web):
        access_web[1].login(LoginData.error_msg_from_wrong_username_data['username'], LoginData.error_msg_from_wrong_username_data['pwd'])
        # 断言
        assert (access_web[1].error_msg_from_wrong_username(), LoginData.error_msg_from_wrong_username_data['excepted'])

    # 登录成功  # fixture的函数名称作为用例参数，用来接收它的返回值
    def test_login_d_success(self, access_web):
        # 步骤  输入用户名、密码 点击登录
        access_web[1].login(LoginData.login_success_data['username'], LoginData.login_success_data['pwd'])
        # 断言 在首页中能否找到退出元素
        assert (IndexPage(access_web[0]).isExist_logout_ele())

# unittest
'''
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from ddt import ddt,data
from TestDatas.login_data import LoginData
from TestDatas.common_data import DoUrl


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 通过Excel读取本功能当中的所有测试数据
        print('========所有测试用例之前执行，只执行一次========')
        cls.driver = webdriver.Chrome()
        cls.driver.get(DoUrl.login_url)
        cls.lp = LoginPage(cls.driver)

    def setUp(self):
        # 前置 打开浏览器，访问登录页面
        pass

    # 登录成功
    def test_login_d_success(self):
        # 步骤
        self.lp.login(LoginData.login_success_data['username'], LoginData.login_success_data['pwd'])
        # 断言 能否找到退出元素
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())

    # 用户名或密码为空
    @data(*LoginData.error_msg_from_login_box_data)
    def test_login_a_null_username_pwd(self, item):
        # 步骤 ddt
        self.lp.login(item['username'], item['pwd'])
        # 断言
        self.assertEqual(self.lp.error_msg_from_login_box(), item['excepted'])

    # 密码错误
    def test_login_b_wrong_pwd(self):
        self.lp.login(LoginData.error_msg_from_wrong_pwd_data['username'],LoginData.error_msg_from_wrong_pwd_data['pwd'])
        # 断言
        self.assertEqual(self.lp.error_msg_from_wrong_pwd(),LoginData.error_msg_from_wrong_pwd_data['excepted'])

    # 用户名错误
    def test_login_c_wrong_username(self):
        self.lp.login(LoginData.error_msg_from_wrong_username_data['username'],
                      LoginData.error_msg_from_wrong_username_data['pwd'])
        # 断言
        self.assertEqual(self.lp.error_msg_from_wrong_username(),LoginData.error_msg_from_wrong_username_data['excepted'])

    @classmethod
    def tearDownClass(cls):
        print('========所有测试用例之后执行，只执行一次========')
        cls.driver.quit()

    def tearDown(self):
        # 每条用例之后刷新页面
        self.driver.refresh()
'''
