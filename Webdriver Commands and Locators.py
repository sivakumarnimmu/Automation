import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-1"]').send_keys("sivakumar")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Nimmu")
driver.find_element(By.NAME, "RESULT_TextField-3").send_keys(9704851471)
driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label').click()
#time.sleep(3)
#driver.close()