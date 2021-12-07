import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
print(driver.title)
time.sleep(3)
driver.get("https://www.javatpoint.com/")
driver.maximize_window()
print(driver.title)
driver.back()
print(driver.title)
time.sleep(3)
driver.forward()
time.sleep(3)
driver.close()
