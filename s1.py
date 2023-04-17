import time

from selenium import webdriver
from selenium.webdriver.common.by import  By
url="http://www.baidu.com"
driver = webdriver.Chrome()#创建浏览对象
driver.get(url)#打开页面
driver.maximize_window()#最大化页面窗口
time.sleep(5)
driver.find_element(By.ID,"kw").send_keys("秦霄贤")#找到搜索框
time.sleep(1)
driver.find_element(By.ID,"su").click()

time.sleep(30)#停留30秒



driver.quit()