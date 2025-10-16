from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://practice-automation.com/click-events/")

try:
    # Ждем и переключаемся в iframe
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "iframe-name"))
    )
    print("✅ Успешно переключились в iframe")
    
    # Тестируем кнопки
    animals = ["Cat", "Dog", "Pig", "Cow"]
    
    for animal in animals:
        # Находим и кликаем кнопку
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{animal}')]"))
        )
        button.click()
        
        # Читаем результат
        result = driver.find_element(By.ID, "demo").text
        print(f"🎯 {animal}: {result}")
        
    print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    
finally:
    time.sleep(3)
    driver.quit()