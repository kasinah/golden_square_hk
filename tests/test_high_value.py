from lib.high_value import HighValue

def test_get_highest_first_higher():
    hv = HighValue(10, 5)
    assert hv.get_highest() == "First value is higher"