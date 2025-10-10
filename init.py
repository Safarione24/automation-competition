from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://practice-automation.com/form-fields/")
time.sleep(2)

naming = driver.find_element(By.NAME, "name-input") 
naming.send_keys('pizda')
time.sleep(2)

password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password.send_keys('123321')
time.sleep(2)

drunk = driver.find_element(By.ID, "drink2")
drunk.click()
time.sleep(2)

color = driver.find_element(By.ID, "color3")
color.click()
time.sleep(2)

like_auto = driver.find_element(By.ID, "automation")
select = Select(like_auto)
select.select_by_value(value="yes") 
time.sleep(2)

email = driver.find_element(By.ID, "email") 
email.send_keys('pizda@mail.ru')
time.sleep(2)

ul_element = driver.find_element(By.TAG_NAME, "ul")
li_elements = ul_element.find_elements(By.TAG_NAME, "li")
tool_texts = [item.text for item in li_elements]
combined_text = ", ".join(tool_texts)

message = driver.find_element(By.NAME, "message") 
message.send_keys(combined_text)
time.sleep(2)

sumbit = driver.find_element(By.ID, "submit-btn")
sumbit.click()
time.sleep(2)

time.sleep(5)
driver.quit()