# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class IndexPage:

    def __init__(self, driver):
        self.driver = driver

    # 查找是否有退出元素
    def isExist_logout_ele(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//a[@id="Logout"]')))
            return True
        except:
            return False
