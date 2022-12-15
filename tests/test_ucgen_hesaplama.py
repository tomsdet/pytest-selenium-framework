def cevre_hesaplama(a,b,c):
    return a+b+c

def alan_hesaplama(taban, yukseklik):

    return (taban * yukseklik) / 2

def test_ucgen_cevresi_hesaplama():
    print("ucgen cevre hesaplama")
    assert cevre_hesaplama(2,3,3) == 8

def test_ucgen_alan_hesaplama():
    print("ucgen alan hesaplama")
    assert alan_hesaplama(4,3) == 6