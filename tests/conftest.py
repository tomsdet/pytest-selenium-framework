from selenium import webdriver
from selenium.webdriver.safari.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest

@pytest.fixture(scope="class")
def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "safari": #bu projede safari kullanilmadi, ornek icin konuldu
        service = Service("./drivers/safari")
        driver = webdriver.Chrome(service=service)
    else:
        print("heeey dogru durust bir tarayici gir")
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
