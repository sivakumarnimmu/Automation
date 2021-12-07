from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# initialize Chrome Browser
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
# Open Browser
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/")
# Maximize Window
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 1000)","")
time.sleep(3)
driver.execute_script("window.scrollTo(0, -1000)","")
