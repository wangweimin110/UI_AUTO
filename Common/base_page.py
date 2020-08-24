# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import datetime
import time
import logging
from Common.congfig_path import *

# 封装基本函数- 执行日志、异常处理、失败截图
# 所有页面的公共部分


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见  locator(定位表达式)
    def wait_element_visible(self, locator, wait_times=30, poll_frequency=0.5, doc=''):
        logging.info('等待元素{}可见'.format(locator))
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(ec.visibility_of_element_located(locator))
            # 结束等待时间
            end = datetime.datetime.now()
            # 求一个差值，写在日志中，等待了多久
            times = (end - start).seconds
            logging.info('{0}：元素{1}可见，等待开始时间:{2}，等待结束时间:{3}，等待时长为：{4}'.format(doc, locator, start, end, times))
        except:
            logging.exception('等待元素可见异常')
            # 截图 -保存到指定目录
            self.error_screenshot(doc)
            # 抛出异常
            raise

    # 等待元素存在
    def wait_element_presence(self, locator, times=30, poll_frequency=0.5, doc=''):
        logging.info('等待元素{}存在'.format(locator))
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(ec.presence_of_element_located(locator))
            # 结束等待时间
            end = datetime.datetime.now()
            # 求一个差值，写在日志中，等待了多久
            wait_times = (end - start).seconds
            logging.info('{0}：元素{1}存在，等待开始时间:{2}，等待结束时间:{3}，等待时长为：{4}'.format(doc, locator, start, end, wait_times))
        except:
            logging.exception('等待元素存在异常')
            # 截图 -保存到指定目录
            self.error_screenshot(doc)
            # 抛出异常
            raise

    # 查找元素
    def get_element(self, locator, doc=''):
        logging.info('查找元素：{}'.format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception('查找元素失败！')
            #截图
            self.error_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=''):
        # 查找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info('点击元素{}'.format(locator))
        try:
            ele.click()
        except:
            logging.exception('点击元素失败！')
            # 截图
            self.error_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=''):
        # 查找元素
        ele = self.get_element(locator,doc)
        # 元素操作
        logging.info('{0}点击输入{1}'.format(locator,text))
        try:
            ele.send_keys(text)
        except:
            logging.exception('元素输入失败！')
            # 截图
            self.error_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=''):
        # 查找元素
        ele = self.get_element(locator,doc)
        # 元素操作
        logging.info('获取元素{}文本内容'.format(locator))
        try:
            return ele.text
        except:
            logging.exception('获取元素文本内容失败！')
            # 截图
            self.error_screenshot(doc)
            raise

        pass

    # 获取元素的属性
    def get_element_attribute(self, locator, attr_name, doc=''):
        # 查找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info('获取元素{}属性'.format(locator))
        try:
            return ele.get_attribute(attr_name)
        except:
            logging.exception('获取元素属性失败！')
            # 截图
            self.error_screenshot(doc)
            raise

    # aletr处理
    def alert_action(self,action='accept'):
        pass

    # iframe切换
    def switch_iframe(self,iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    def scrollbar_action(self):
        pass

    # 截图
    def error_screenshot(self,doc):
        # 图片名称：模块名_页面名称_操作名称_时间(年月日时分秒).png
        # file_path = 指的是图片保存目录/model（页面功能名称）_当前时间到秒.png
        file_path = screenshot_path + \
                    '/{0}_{1}.png'.format(doc, time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()))
        # 截图存放在screenshot目录下
        try:
            self.driver.save_screenshot(file_path)
            logging.info('截图成功，路径为：{}'.format(file_path))
        except:
            logging.exception('截图失败')
