import re
from selenium.webdriver.common.by import By


class UrunDetaySayfasi:

    def __init__(self, driver):
        self.driver = driver

    def sepetteki_urun_sayisini_ver(self):
        sepetteki_urun_sayisi = self.driver.find_element(By.CSS_SELECTOR, "a.ico-cart span:nth-child(2)").text
        sepetteki_urun_sayisi = re.findall(r'\d+', sepetteki_urun_sayisi)
        return int(sepetteki_urun_sayisi[0])

    def quantity_sayisini_ver(self):
        quantity = self.driver.find_element(By.CSS_SELECTOR, "input[id$='EnteredQuantity']").get_attribute('value')
        return int(re.findall(r'\d+', quantity)[0])

    def add_to_cart_buttona_tikla(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[id^='add-to-cart-button']").click()

    def urun_ismini_ver(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.product-name h1").text.strip()

    def urun_fiyatini_ver(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.product-price span").text.strip()