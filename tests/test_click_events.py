import pytest
import allure
from pages.click_events_page import ClickEventsPage

@allure.epic("Click Events Tests")
@allure.feature("Mouse Events Functionality")
class TestClickEvents:
    
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.page = ClickEventsPage(browser)
        self.page.open()
        yield
        # Cleanup if needed
    
    @allure.story("Single Click Test")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test that single click on button produces expected result")
    def test_single_click(self):
        with allure.step("Perform single click and verify result"):
            self.page.click_button()
            result = self.page.get_click_result()
            assert "Click" in result, f"Expected 'Click' in result, but got: {result}"
    
    @allure.story("Double Click Test")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test that double click on button produces expected result")
    def test_double_click(self):
        with allure.step("Perform double click and verify result"):
            self.page.double_click_button()
            result = self.page.get_double_click_result()
            assert "Double" in result, f"Expected 'Double' in result, but got: {result}"
    
    @allure.story("Hover Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test that hover over button produces expected result")
    def test_hover(self):
        with allure.step("Perform hover and verify result"):
            self.page.hover_button()
            result = self.page.get_hover_result()
            assert "Hover" in result, f"Expected 'Hover' in result, but got: {result}"
    
    @allure.story("Mouse Down Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test that mouse down on button produces expected result")
    def test_mouse_down(self):
        with allure.step("Perform mouse down and verify result"):
            self.page.mouse_down_button()
            result = self.page.get_mouse_down_result()
            assert "Mouse" in result, f"Expected 'Mouse' in result, but got: {result}"
    
    @allure.story("Right Click Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test that right click on button produces expected result")
    def test_right_click(self):
        with allure.step("Perform right click and verify result"):
            self.page.right_click_button()
            result = self.page.get_right_click_result()
            assert "Right" in result, f"Expected 'Right' in result, but got: {result}"
    
    @allure.story("All Events Test")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test all click events in sequence")
    def test_all_click_events(self):
        with allure.step("Test all click events in sequence"):
            # Single click
            self.page.click_button()
            click_result = self.page.get_click_result()
            assert "Click" in click_result
            
            # Double click
            self.page.double_click_button()
            dbl_click_result = self.page.get_double_click_result()
            assert "Double" in dbl_click_result
            
            # Hover
            self.page.hover_button()
            hover_result = self.page.get_hover_result()
            assert "Hover" in hover_result
            
            # Mouse down
            self.page.mouse_down_button()
            mousedown_result = self.page.get_mouse_down_result()
            assert "Mouse" in mousedown_result
            
            # Right click
            self.page.right_click_button()
            right_click_result = self.page.get_right_click_result()
            assert "Right" in right_click_result