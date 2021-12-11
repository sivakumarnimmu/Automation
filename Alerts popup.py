from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize Chrome browser
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
# Open Browser
driver.get("http://demo.guru99.com/V1/index.php")
# maximize Window
driver.maximize_window()
driver.find_element(By.NAME, "btnLogin").click()
time.sleep(3)
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()
time.sleep(3)
driver.close()
