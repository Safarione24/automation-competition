from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pytest

def test_form_fields():
    driver = webdriver.Chrome()
    driver.get("https://practice-automation.com/form-fields/")
    
    try:
        # ЗАПОЛНИТЬ ФОРМУ
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
        driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", color)
        time.sleep(2)

        like_auto = driver.find_element(By.ID, "automation")
        select = Select(like_auto)
        select.select_by_value(value="yes") 
        time.sleep(2)

        email = driver.find_element(By.ID, "email") 
        email.send_keys('pizda@mail.ru')
        time.sleep(2)

        automation_lists = driver.find_elements(By.TAG_NAME, "ul")
        tools_list = automation_lists[1]
        tool_items = tools_list.find_elements(By.TAG_NAME, "li")
        tools_text = [tool.text for tool in tool_items]
 
        message_field = driver.find_element(By.ID, "message")
        message_field.send_keys("\n".join(tools_text))
        message_value = message_field.get_attribute("value")
        assert "Selenium" in message_value
        time.sleep(2)

        # ФИКС ДЛЯ SUBMIT КНОПКИ
        submit = driver.find_element(By.ID, "submit-btn")
        driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", submit)
        time.sleep(2)
        
        # ПРОВЕРИТЬ РЕЗУЛЬТАТ
        alert = driver.switch_to.alert
        assert "Message received" in alert.text
        alert.accept()
        
    finally:
        driver.quit()