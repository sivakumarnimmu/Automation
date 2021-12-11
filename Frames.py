from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize Chrome browser
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
# Open Browser
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
# maximize Window
driver.maximize_window()
# First Frame
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(3)
driver.switch_to.default_content()
# second Frame
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
time.sleep(3)
driver.switch_to.default_content()
# Third Frame
driver.switch_to.frame("classFrame")
driver.find_element(By.LINK_TEXT, "INDEX").click()