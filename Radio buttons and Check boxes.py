from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# initialize Chrome Browser
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
# Open Browser
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/")
# Maximize Window
driver.maximize_window()
# Check total input boxes
IPT=driver.find_elements(By.CLASS_NAME, "text_field")
print(len(IPT))
# Verify Text is enabled or not
Enable=driver.find_element(By.ID, "RESULT_TextField-1").is_enabled()
print(Enable)
# Verify Text is displayed or not
Display=driver.find_element(By.ID, "RESULT_TextField-1").is_displayed()
print(Display)
# Enter all Text fields Data
driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Sivakumar")
driver.find_element(By.NAME, "RESULT_TextField-2").send_keys("Nimmu")
driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-3"]').send_keys(9704851471)
driver.find_element(By.ID, "RESULT_TextField-4").send_keys("INDIA")
driver.find_element(By.NAME, "RESULT_TextField-5").send_keys("Hyderabad")
driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-6"]').send_keys("sivakumar.nimmu@gmail.com")
# Verify Radio button enabled or not
RBS=driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[2]/td/label').is_selected()
print(RBS)
# Click on radio button
driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[2]/td/label').click()
time.sleep(2)
# Click on Check boxes
driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[5]/td/label').click()
driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[2]/td/label').click()
time.sleep(2)
# Check Dropdowns
element=driver.find_element(By.ID, "RESULT_RadioButton-9")
drp=Select(element)
#drp.select_by_visible_text("Afternoon")
#drp.select_by_value("Radio-2")
drp.select_by_index(1)
print(len(drp.options))
all_options=drp.options
for options in all_options:
    print(options.text)
# Capture Screenshot
driver.save_screenshot("C:\Driver\homepage.png")
time.sleep(3)
# File Upload
ULF=driver.find_element(By.XPATH, "//input[@name='RESULT_FileUpload-10']")
ULF.send_keys("C:\\Driver\\homepage.png")
time.sleep(3)
driver.close()

