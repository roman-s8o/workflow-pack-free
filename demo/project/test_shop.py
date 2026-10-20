from shop import total

def test_no_discount():
    assert total([10, 20]) == 30

def test_percent_discount():
    assert total([100], 10) == 90

def test_percent_discount_not_flat():
    assert total([50], 10) == 45

def test_zero_price_list():
    assert total([], 10) == 0
    assert total([0, 0], 10) == 0
