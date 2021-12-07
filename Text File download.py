from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="textbox"]').send_keys("Enter Text")
driver.find_element(By.XPATH, '//*[@id="createTxt"]').click()
driver.find_element(By.ID, "link-to-download").click()