import time

import pytest
from selenium.webdriver.common.by import By
import re

@pytest.mark.usefixtures("setup")
class TestUrunDetaylari:

    def test_add_to_cart_button_adds_product_to_cart(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.find_element(By.XPATH, "//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]").click()
        sepetteki_urun_sayisi = self.driver.find_element(By.CSS_SELECTOR, "a.ico-cart span:nth-child(2)").text
        sepetteki_urun_sayisi = re.findall(r'\d+', sepetteki_urun_sayisi)
        oncesi = int(sepetteki_urun_sayisi[0])
        quantity = self.driver.find_element(By.CSS_SELECTOR, "input[id$='EnteredQuantity']").get_attribute('value')
        quantity = int(re.findall(r'\d+', quantity)[0])

        self.driver.find_element(By.CSS_SELECTOR, "input[id^='add-to-cart-button']").click()
        time.sleep(1) # sepetteki urun sayisinin degismesini bekliyor

        sepetteki_urun_sayisi = self.driver.find_element(By.CSS_SELECTOR, "a.ico-cart span:nth-child(2)").text
        sepetteki_urun_sayisi = re.findall(r'\d+', sepetteki_urun_sayisi)
        sonrasi = int(sepetteki_urun_sayisi[0])

        assert sonrasi ==  (oncesi + quantity)
