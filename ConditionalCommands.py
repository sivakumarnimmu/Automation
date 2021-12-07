import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
user_ele=driver.find_element(By.NAME, "userName")
print(user_ele.is_enabled())
print(user_ele.is_displayed())
pwd_ele=driver.find_element(By.NAME, "password")
print(pwd_ele.is_enabled())
print(pwd_ele.is_displayed())
user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
time.sleep(2)
driver.find_element(By.NAME, "submit").click()