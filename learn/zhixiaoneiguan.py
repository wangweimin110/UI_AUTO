# coding = utf - 8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

url = 'http://103.160.51.63:9080/hxdsbank/inner/userservices/loginPage-view.html'
username = 'zhwwm'
pwd = 'Qqqq1111'

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.refresh()
time.sleep(3)
xpath = '//*[@id="operNo"]/input'
WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,xpath)))
driver.find_element_by_xpath('//*[@id="operNo"]/input').send_keys(username)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="operNo"]/input').send_keys(Keys.CONTROL,'a')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="operNo"]/input').send_keys(Keys.CONTROL,'x')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="operNo"]/input').send_keys(Keys.CONTROL,'v')
ele = driver.find_element_by_xpath('//*[@id="loginPwd"]/input')
ele.send_keys(pwd)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginButton"]').click()

