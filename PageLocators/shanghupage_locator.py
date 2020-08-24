# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class ShanghuPageLocator:
    '''元素定位'''
    #商户管理
    business_management = (By.XPATH,'//span[text()="商户管理"]')
    #商户签约维护
    mcm = (By.XPATH,"//span[text()='商户签约维护']")
    #商户编号
    merchant_id = (By.XPATH,'//*[@id="nuiPageLoad280query_id"]/input')
    