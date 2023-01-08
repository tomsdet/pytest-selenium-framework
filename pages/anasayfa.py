from selenium.webdriver.common.by import By


class  Anasayfa:

    def __init__(self, driver):
        self.driver = driver

    def ust_menu_isimlerini_liste_ver(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, "ul.top-menu > li > a")
        actual_menu_items = []
        for i in elements:
            actual_menu_items.append(i.text)

        return actual_menu_items

    def ilk_urun_ismini_ver(self):
        ilk_urun_linki = self.driver.find_element(By.CSS_SELECTOR, "div.product-item h2 a")
        return ilk_urun_linki.text

    def ilk_urun_fiyatini_ver(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span.price.actual-price").text

    def ilk_urun_ismine_tikla(self):
        self.driver.find_element(By.CSS_SELECTOR, "div.product-item h2 a").click()

    def gift_card_olmayan_ilk_urun_ismine_tikla(self):
        self.driver.find_element(By.XPATH, "//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]").click()