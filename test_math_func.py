import main

def test_add():
    assert main.add(7, 3) == 10
    assert main.add(7) == 9
    assert main.add(5) == 7

def test_product():
    assert main.product(5, 3) == 15
    assert main.product(5) == 10
    assert main.product(7) == 14