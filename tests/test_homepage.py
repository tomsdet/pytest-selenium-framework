from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestHomepage:
    def test_top_menu_items(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")
        expected_menu = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS",
                         "JEWELRY", "GIFT CARDS"]
        elements = driver.find_elements(By.CSS_SELECTOR, "ul.top-menu > li > a")
        actual_menu_items = []

        for i in elements:
            actual_menu_items.append(i.text)

        for i in range(len(expected_menu)):
            assert expected_menu[i] == actual_menu_items[i]

        driver.quit()