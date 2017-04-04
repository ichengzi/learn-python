# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

el = driver.find_element_by_id('kw')
el.send_keys('chengzi'+Keys.RETURN)
time.sleep(1)
print driver.title

# 返回百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

name = input("please input :")
driver.quit()