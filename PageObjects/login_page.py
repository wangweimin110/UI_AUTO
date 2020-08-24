# -*- coding: utf-8 -*-

from PageLocators.loginpage_locator import LoginPageLocator as LPL
from Common.base_page import BasePage


class LoginPage(BasePage):
    # 登录
    def login(self, username, pwd):
        self.driver.refresh()
        self.driver.maximize_window()
        # 输入用户名
        # 输入密码
        doc = '登录页面_登录功能'
        self.wait_element_visible(LPL.login_name_text, doc=doc)
        self.input_text(LPL.login_name_text, username, doc)
        self.input_text(LPL.login_pwd_text, pwd, doc)
        self.click_element(LPL.login_but, doc)
        # WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(LoginPageLocator.login_name_text))
        # self.driver.find_element(*LoginPageLocator.login_name_text).send_keys(username)
        # self.driver.find_element(*LoginPageLocator.login_pwd_text).send_keys(pwd)
        # 如果有记住密码/用户名勾选框 添加一个remeber_user=Ture参数，判断他的值，是否勾选
        # self.driver.find_element(*LoginPageLocator.login_but).click()

    # 注册入口
    # def register_enter(self):
    #     self.wait_element_visible(LPL.'注册定位', doc)
    #     self.click_element(LPL.'注册定位', doc)

    # 密码错误
    def error_msg_from_wrong_pwd(self):
        doc = '登录页面_密码输入错误提示'
        self.wait_element_visible(LPL.msg_from_wrong_pwd, poll_frequency=0.2, doc=doc)
        return self.get_text(LPL.msg_from_wrong_pwd, doc)
        # WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH
        #                                 ,'//span[contains(text(), "DSIE0011:账号或密码错误")]')))
        # return self.driver.find_element_by_xpath('//span[contains(text(), "DSIE0011:账号或密码错误")]').text

    # 用户名错误
    def error_msg_from_wrong_username(self):
        doc = '登录页面_用户名输入错误提示'
        self.wait_element_visible(LPL.msg_from_wrong_username,poll_frequency=0.2, doc=doc)
        return self.get_text(LPL.msg_from_wrong_username, doc)
        # WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH
        #                             ,'//span[contains(text(), "DSIE0104:操作员不存在")]')))
        # return self.driver.find_element_by_xpath('//span[contains(text(), "DSIE0104:操作员不存在")]').text

    # 密码/用户名为空
    def error_msg_from_login_box(self):
        doc = '登录页面_密码/用户名为空错误提示'
        self.wait_element_visible(LPL.msg_from_login_box, doc=doc)
        return self.get_text(LPL.msg_from_login_box, doc)
        # WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH
        #                                 ,'//div[@class="error_info"]')))
        # return self.driver.find_element_by_xpath('//div[@class="error_info"]').text

    # 注册
    def register(self):
        pass



