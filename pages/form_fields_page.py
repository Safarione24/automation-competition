from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class FormFieldsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practice-automation.com/form-fields/"
        
        # ЛОКАТОРЫ
        self.name_input = (By.NAME, "name-input")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.drink2_radio = (By.ID, "drink2")
        self.color3_checkbox = (By.ID, "color3")
        self.automation_select = (By.ID, "automation")
        self.email_input = (By.ID, "email")
        self.message_field = (By.ID, "message")
        self.submit_btn = (By.ID, "submit-btn")
    
    def open(self):
        """Открыть страницу"""
        self.driver.get(self.url)
    
    def fill_name(self, name):
        """Заполнить поле Name"""
        self.driver.find_element(*self.name_input).send_keys(name)
    
    def fill_password(self, password):
        """Заполнить поле Password"""
        self.driver.find_element(*self.password_input).send_keys(password)
    
    def select_drink(self):
        """Выбрать напиток"""
        self.driver.find_element(*self.drink2_radio).click()
    
    def select_color(self):
        """Выбрать цвет (с JS кликом)"""
        color = self.driver.find_element(*self.color3_checkbox)
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", color)
    
    def select_automation_like(self, value="yes"):
        """Выбрать отношение к автоматизации"""
        select = Select(self.driver.find_element(*self.automation_select))
        select.select_by_value(value)
    
    def fill_email(self, email):
        """Заполнить email"""
        self.driver.find_element(*self.email_input).send_keys(email)
    
    def copy_automation_tools(self):
        """Скопировать список Automation Tools в Message"""
        # Найти второй список ul на странице
        lists = self.driver.find_elements(By.TAG_NAME, "ul")
        tools_list = lists[1]
        
        # Получить текст всех li элементов
        tool_items = tools_list.find_elements(By.TAG_NAME, "li")
        tools_text = [tool.text for tool in tool_items]
        
        # Вставить в поле Message
        self.driver.find_element(*self.message_field).send_keys("\n".join(tools_text))
        
        # Вернуть текст для проверки
        return tools_text
    
    def submit_form(self):
        """Отправить форму (с JS кликом)"""
        submit = self.driver.find_element(*self.submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", submit)
    
    def get_alert_text(self):
        """Получить текст alert"""
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text
    
    # ОСНОВНОЙ МЕТОД - заполнить всю форму
    def fill_complete_form(self, name, password, email):
        """Заполнить всю форму одним методом"""
        self.fill_name(name)
        self.fill_password(password)
        self.select_drink()
        self.select_color()
        self.select_automation_like("yes")
        self.fill_email(email)
        self.copy_automation_tools()
        self.submit_form()