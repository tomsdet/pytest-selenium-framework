# pytest-selenium-framework
Pytest ve Selenium kullanarak temel web test otomasyon framework kurulumu video serisinin kodlarını içerir. https://www.youtube.com/playlist?list=PLbFzTYWXNlJ5F3L8Z1RIO4NLiyTXa2uZA 

Master branch kodun en son halini içerir. Projenin bir ders anındaki halini o dersin branch inde bulabilirsiniz.

# Terminalden (command line) testleri çalıştırmak

pytest = projedeki tüm testleri çalıştırır.

pytest -v = projedeki tüm testleri çalıştırır. Hangi dosyada hangi testin çalıştığını sonucuyla (FAILED/PASSED) verir

pytest -vs = projedeki tüm testleri ve print() mesajlarını konsola yazdırır

pytest -q = sessiz mod. Tüm testleri çalıştırır ama konsola sadece kaç test FAILED ve PASSED olduğunu yazar

pytest tests/test_ucgen_hesaplama.py = sadece bir dosyadaki testleri çalıştırır

pytest -k alan = Projenin tamamında fonksiyon adında verilen keyword (alan) geçen testleri çalıştırır
