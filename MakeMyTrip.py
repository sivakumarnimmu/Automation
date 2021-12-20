from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Initialize Chrome browser
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
# Open Browser
driver.get("https://www.makemytrip.com/")
# Maximize Window
driver.maximize_window()
driver.implicitly_wait(5)
# Remove Pop-up
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/main[1]/div[8]/span[1]").click()
driver.find_element(By.XPATH, "//*[@id='SW']/div[1]/div[1]/ul/li[3]").click()
time.sleep(2)
# click on RoundTrip
roundtrip=driver.find_element(By.XPATH, "//*[text()='Round Trip']")
roundtrip.click();
time.sleep(5)
# Select From City
driver.find_element(By.XPATH, "//span[text()='From']").click()
From=driver.find_element(By.XPATH, "//input[@placeholder='From']")
time.sleep(3)
From.send_keys("Hyderabad")
time.sleep(2)
From.send_keys(Keys.DOWN)
From.send_keys(Keys.ENTER)
time.sleep(2)
# Select To City
driver.find_element(By.XPATH, "//span[text()='To']").click()
To=driver.find_element(By.XPATH, "//input[@placeholder='To']")
To.send_keys("Bengalore")
time.sleep(2)
To.send_keys(Keys.DOWN)
To.send_keys(Keys.ENTER)
time.sleep(2)
# Select and click on Departure
driver.find_element(By.XPATH, "//span[contains(text(),'DEPARTURE')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[5]/div[5]/div[1]/p[1]").click()
# Select and click on Return
driver.find_element(By.XPATH, "//span[contains(text(),'RETURN')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[4]/div[5]/div[1]/p[1]").click()
time.sleep(1)
# Click on Search
driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
time.sleep(2)
# Select Services
driver.find_element(By.XPATH, "//span[@class='box']").click()
driver.execute_script("window.scrollTo(0, 500)","")
# Select Flight
driver.find_element(By.XPATH, "//div[@id='root']").click()
time.sleep(2)
# Book Flight
driver.find_element(By.XPATH, "//div[@class='makeFlex hrtlCenter gap-x-10']//*[text()='Book Now']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[text()='Continue']").click()
time.sleep(3)
# prints the window handle in focus
#print(driver.current_window_handle)
# to fetch the first child window handle
chwnd = driver.window_handles[1]
# to switch focus the first child window handle
driver.switch_to.window(chwnd)
time.sleep(3)
MN=driver.find_element(By.XPATH, "//input[@placeholder='Mobile No']")
time.sleep(2)
MN.send_keys(9704851471)
time.sleep(1)
MN.send_keys(Keys.TAB)
Mob=driver.find_element(By.XPATH, "//input[@placeholder='Email']")
Mob.send_keys("sivakumar.nimmu@gmail.com")
time.sleep(2)
Mob.send_keys(Keys.DOWN)
Mob.send_keys(Keys.ENTER)
time.sleep(2)
#driver.find_element(By.XPATH, "//*[@id='mainSection_0']/div[5]/button").click()
driver.quit()
