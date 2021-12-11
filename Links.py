from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# initialize Chrome browser
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
# Open Browser
driver.get("http://demo.guru99.com/test/newtours/")
# maximize Window
driver.maximize_window()
# find number of links in the page
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
# list the link Names
for link in links:
    print(link.text)
time.sleep(3)
# Click on links by Link Text
# driver.find_element(By.LINK_TEXT, "REGISTER").click()
# Click on links by Partial Link Text
driver.find_element(By.PARTIAL_LINK_TEXT, "SUPP").click()
time.sleep(3)
driver.close()
