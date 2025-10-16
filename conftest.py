import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import allure

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser", default="chrome")
    
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.implicitly_wait(10)
    
    yield driver
    
    # Take screenshot on failure
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{request.node.name}_failure",
                attachment_type=allure.attachment_type.PNG
            )
        except:
            pass
    
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome or firefox")