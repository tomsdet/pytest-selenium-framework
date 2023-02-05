from selenium import webdriver
from selenium.webdriver.safari.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest


@pytest.fixture(scope="class")
def setup(request, browser, environment):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "safari": #bu projede safari kullanilmadi, ornek icin konuldu
        service = Service("./drivers/safari")
        driver = webdriver.Chrome(service=service)
    else:
        print("heeey dogru durust bir tarayici gir")

    if environment is None:
        print("environment girmeyi unutmayin diye kac kere soyledik")
    else:
        if environment == "dev":
            base_url = "https://dev-demowebshop.tricentis.com"
        elif environment == "qa":
            base_url = "https://qa-demowebshop.tricentis.com"
        elif environment == "test":
            base_url = "https://test-demowebshop.tricentis.com"
        elif environment == "prod":
            base_url = "https://demowebshop.tricentis.com"
        else:
            print("Environment degeri hatali. Lutfen parametreyi kontol edin")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.baseurl = base_url
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--env")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def environment(request):
    return request.config.getoption("--env")
