from selenium.webdriver.common.by import By

from pages.PageBase import PageBase
from pages.urun_detay_sayfasi import UrunDetaySayfasi


class  Anasayfa(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    UST_MENU_LINKLERI  = (By.CSS_SELECTOR, "ul.top-menu > li > a")
    ILK_URUN_ISMI = (By.CSS_SELECTOR, "div.product-item h2 a")
    ILK_GIFT_CARD_OLMAYAN_URUN_ISMI = (By.XPATH, "//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]")
    ILK_URUN_FIYATI = (By.CSS_SELECTOR, "span.price.actual-price")

    def ust_menu_isimlerini_liste_ver(self):
        return self.webelement_listesinden_string_listesi_ver(Anasayfa.UST_MENU_LINKLERI)

    def ilk_urun_ismini_ver(self):
        ilk_urun_linki = self.driver.find_element(*Anasayfa.ILK_URUN_ISMI)
        return ilk_urun_linki.text

    def ilk_urun_fiyatini_ver(self):
        return self.driver.find_element(*Anasayfa.ILK_URUN_FIYATI).text

    def ilk_urun_ismine_tikla(self):
        ilk_urun_ismi = self.wait_element_visibility(Anasayfa.ILK_URUN_ISMI)
        ilk_urun_ismi.click()
        urun_detay_sayfasi = UrunDetaySayfasi(self.driver)
        return urun_detay_sayfasi

    def gift_card_olmayan_ilk_urun_ismine_tikla(self):
        urun_detay_sayfasi = UrunDetaySayfasi(self.driver)
        self.driver.find_element(*Anasayfa.ILK_GIFT_CARD_OLMAYAN_URUN_ISMI).click()
        return urun_detay_sayfasi