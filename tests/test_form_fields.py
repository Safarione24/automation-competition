import allure
from selenium import webdriver
from pages.form_fields_page import FormFieldsPage

@allure.epic("Practice Automation")
@allure.feature("Form Fields")
@allure.story("Complete Form Submission")
class TestFormFields:
    
    @allure.title("Fill and submit complete form")
    @allure.description("Test complete form filling with all fields and verify success alert")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_form_fields(self):
        driver = webdriver.Chrome()
        page = FormFieldsPage(driver)
        
        try:
            with allure.step("Open form fields page"):
                page.open()
                allure.attach(driver.get_screenshot_as_png(), name="page_opened", attachment_type=allure.attachment_type.PNG)
            
            with allure.step("Fill name field"):
                page.fill_name("Safarmon")
            
            with allure.step("Fill password field"):
                page.fill_password("SecurePass123")
            
            with allure.step("Select drink option"):
                page.select_drink()
            
            with allure.step("Select color checkbox"):
                page.select_color()
            
            with allure.step("Select automation preference"):
                page.select_automation_like("yes")
            
            with allure.step("Fill email field"):
                page.fill_email("test@example.com")
            
            with allure.step("Copy automation tools to message"):
                tools = page.copy_automation_tools()
                allure.attach(str(tools), name="automation_tools", attachment_type=allure.attachment_type.TEXT)
            
            with allure.step("Submit form"):
                page.submit_form()
            
            with allure.step("Verify success alert"):
                alert_text = page.get_alert_text()
                allure.attach(alert_text, name="alert_text", attachment_type=allure.attachment_type.TEXT)
                assert "Message received" in alert_text
                
            with allure.step("Test completed successfully"):
                print("✅ ТЕСТ ПРОЙДЕН!")
                
        except Exception as e:
            # Скриншот при ошибке
            driver.save_screenshot("error.png")
            allure.attach.file("error.png", name="error_screenshot", attachment_type=allure.attachment_type.PNG)
            raise e
            
        finally:
            driver.quit()