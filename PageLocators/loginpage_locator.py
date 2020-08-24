# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class LoginPageLocator:
    '''元素定位'''

    # 用户名输入框
    login_name_text = (By.XPATH, '//*[@id="operNo"]/input')
    # 密码输入框
    login_pwd_text = (By.XPATH, '//*[@id="loginPwd"]/input')
    # 登录按钮
    login_but = (By.XPATH, '//*[@id="loginButton"]')
    # 密码输入错误提示
    msg_from_wrong_pwd = (By.XPATH, '//span[contains(text(), "DSIE0011:账号或密码错误")]')
    # 用户名错误
    msg_from_wrong_username = (By.XPATH, '//span[contains(text(), "DSIE0104:操作员不存在")]')
    # 密码/用户名为空
    msg_from_login_box = (By.XPATH, '//div[@class="error_info"]')