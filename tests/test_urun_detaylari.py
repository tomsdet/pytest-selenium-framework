import time
import pytest
from pages.anasayfa import Anasayfa
from pages.urun_detay_sayfasi import UrunDetaySayfasi


@pytest.mark.usefixtures("setup")
class TestUrunDetaylari:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.anasayfa = Anasayfa(self.driver)

    def test_add_to_cart_button_adds_product_to_cart(self):
        self.driver.get(self.baseurl)

        urun_detay_sayfasi = self.anasayfa.gift_card_olmayan_ilk_urun_ismine_tikla()
        oncesi = urun_detay_sayfasi.sepetteki_urun_sayisini_ver()
        quantity = urun_detay_sayfasi.quantity_sayisini_ver()
        urun_detay_sayfasi.add_to_cart_buttona_tikla()
        time.sleep(1) # sepetteki urun sayisinin degismesini bekliyor
        sonrasi = urun_detay_sayfasi.sepetteki_urun_sayisini_ver()

        assert sonrasi == (oncesi + quantity)
