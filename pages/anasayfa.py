from selenium.webdriver.common.by import By


class  Anasayfa:

    def __init__(self, driver):
        self.driver = driver

    UST_MENU_LINKLERI  = (By.CSS_SELECTOR, "ul.top-menu > li > a")
    ILK_URUN_ISMI = (By.CSS_SELECTOR, "div.product-item h2 a")
    ILK_GIFT_CARD_OLMAYAN_URUN_ISMI = (By.XPATH, "//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]")
    ILK_URUN_FIYATI = (By.CSS_SELECTOR, "span.price.actual-price")

    def ust_menu_isimlerini_liste_ver(self):
        elements = self.driver.find_elements(*Anasayfa.UST_MENU_LINKLERI)
        actual_menu_items = []
        for i in elements:
            actual_menu_items.append(i.text)

        return actual_menu_items

    def ilk_urun_ismini_ver(self):
        ilk_urun_linki = self.driver.find_element(*Anasayfa.ILK_URUN_ISMI)
        return ilk_urun_linki.text

    def ilk_urun_fiyatini_ver(self):
        return self.driver.find_element(*Anasayfa.ILK_URUN_FIYATI).text

    def ilk_urun_ismine_tikla(self):
        self.driver.find_element(*Anasayfa.ILK_URUN_ISMI).click()

    def gift_card_olmayan_ilk_urun_ismine_tikla(self):
        self.driver.find_element(*Anasayfa.ILK_GIFT_CARD_OLMAYAN_URUN_ISMI).click()