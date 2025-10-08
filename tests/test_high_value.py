from lib.high_value import HighValue

def test_get_highest_first_higher():
    hv = HighValue(10, 5)
    assert hv.get_highest() == "First value is higher"
    hv = HighValue(5, 10)
    assert hv.get_highest() == "Second value is higher"
    hv = HighValue(7, 7)
    assert hv.get_highest() == "Both values are equal"  

def test_add():
    hv = HighValue(10, 5)
    hv.add(3, "first")
    assert hv.value_first == 13
    assert hv.value_second == 5
    hv.add(2, "second")
    assert hv.value_first == 13
    assert hv.value_second == 7
    hv.add(5, "first")
    assert hv.value_first == 18
    assert hv.value_second == 7
    hv.add(10, "second")
    assert hv.value_first == 18
    assert hv.value_second == 17