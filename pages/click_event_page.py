from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class ClickEventsPage(BasePage):
    # Locators
    BUTTON_CLICK = (By.ID, "click")
    BUTTON_DBL_CLICK = (By.ID, "dbl-click")
    BUTTON_HOVER = (By.ID, "hover")
    BUTTON_MOUSEDOWN = (By.ID, "mousedown")
    BUTTON_RIGHT_CLICK = (By.ID, "right-click")
    
    # Result elements
    CLICK_RESULT = (By.ID, "click-result")
    DBL_CLICK_RESULT = (By.ID, "dbl-click-result")
    HOVER_RESULT = (By.ID, "hover-result")
    MOUSEDOWN_RESULT = (By.ID, "mousedown-result")
    RIGHT_CLICK_RESULT = (By.ID, "right-click-result")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://practice-automation.com/click-events/"
    
    def open(self):
        with allure.step("Open Click Events page"):
            self.driver.get(self.url)
    
    @allure.step("Click on Click button")
    def click_button(self):
        self.click(self.BUTTON_CLICK)
    
    @allure.step("Double click on Double Click button")
    def double_click_button(self):
        from selenium.webdriver import ActionChains
        element = self.find_element(self.BUTTON_DBL_CLICK)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(element).perform()
    
    @allure.step("Hover over Hover button")
    def hover_button(self):
        from selenium.webdriver import ActionChains
        element = self.find_element(self.BUTTON_HOVER)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()
    
    @allure.step("Mouse down on Mouse Down button")
    def mouse_down_button(self):
        from selenium.webdriver import ActionChains
        element = self.find_element(self.BUTTON_MOUSEDOWN)
        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(element).perform()
    
    @allure.step("Right click on Right Click button")
    def right_click_button(self):
        from selenium.webdriver import ActionChains
        element = self.find_element(self.BUTTON_RIGHT_CLICK)
        action_chains = ActionChains(self.driver)
        action_chains.context_click(element).perform()
    
    @allure.step("Get click result text")
    def get_click_result(self):
        return self.get_text(self.CLICK_RESULT)
    
    @allure.step("Get double click result text")
    def get_double_click_result(self):
        return self.get_text(self.DBL_CLICK_RESULT)
    
    @allure.step("Get hover result text")
    def get_hover_result(self):
        return self.get_text(self.HOVER_RESULT)
    
    @allure.step("Get mouse down result text")
    def get_mouse_down_result(self):
        return self.get_text(self.MOUSEDOWN_RESULT)
    
    @allure.step("Get right click result text")
    def get_right_click_result(self):
        return self.get_text(self.RIGHT_CLICK_RESULT)