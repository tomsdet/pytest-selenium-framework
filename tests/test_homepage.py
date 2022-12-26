from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestHomepage:
    def test_ust_menu_linklerini_dogrula(self):
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

    def test_urun_ismine_tiklayinca_urun_detaylari_sayfasi_acilir(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")

        ilk_urun_linki = driver.find_element(By.CSS_SELECTOR, "div.product-item h2 a")
        urun_ismi = ilk_urun_linki.text
        urun_fiyati = driver.find_element(By.CSS_SELECTOR, "span.price.actual-price").text
        ilk_urun_linki.click()
        urun_ismi_detay_sayfasi = driver.find_element(By.CSS_SELECTOR, "div.product-name h1").text.strip()
        urun_fiyat_detay_sayfasi = driver.find_element(By.CSS_SELECTOR, "div.product-price span").text.strip()

        assert urun_ismi == urun_ismi_detay_sayfasi
        assert urun_fiyati == urun_fiyat_detay_sayfasi
        driver.quit()

