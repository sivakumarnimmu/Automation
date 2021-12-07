from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
driver.find_element(By.NAME, "userName").send_keys("mercury")
driver.find_element(By.NAME, "password").send_keys("mercury")
driver.find_element(By.NAME, "submit").click()