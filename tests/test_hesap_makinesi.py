def toplama(a, b):
    return a+b;

def cikarma(a,b):
    return a-b;

def bolme(a, b):
    return a/b;

def carpma(a,b):
    return a*b;

def test_toplama():
    assert 4 == toplama(2,2)

def test_cikarma():
    assert cikarma(5,3) == 2

def test_bolme():
    assert bolme(10,5) == 2

def test_carpma():
    assert carpma(3,3) == 9