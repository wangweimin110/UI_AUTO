# coding = UTF - 8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://103.160.224.30:8080/hxqc/techcomp/security/loginProcessor!begin.action')
driver.maximize_window()
driver.find_element_by_id('j_username').send_keys('hw_wangweimin')
driver.find_element_by_id('j_password').send_keys('1')
driver.find_element_by_id('loginButton').click()
time.sleep(2)
driver.find_element_by_xpath('//span[contains(text(),"信息维护")]').click()
driver.find_element_by_xpath('//span[contains(text(),"用户密码修改")]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[@class="hearderBar_image hearderBar_home"]').click()
#ActionChains(driver).move_to_element(above).perform()

time.sleep(2)
above = driver.find_element_by_xpath('//div[@class="hearderBar_user"]')
ActionChains(driver).move_to_element(above).perform()
above.find_element_by_xpath('//span[contains(text(),"退出登录")]').click()