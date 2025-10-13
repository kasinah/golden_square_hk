
from lib.fizzbuzz import *

"""
Given that the number is not divisible by both 3 and 5
it returns number ex: 8
"""
def test_number_not_divisible_by_3_and_5():
    result = fizzbuzz(8)
    assert result == 8

"""
Given that the number is divisible by 3 
it returns number "Fizz"
"""

def test_number_divisible_by_3():
    result = fizzbuzz(3)
    assert result == "Fizz"

"""
Given that the number is divisible by 5 
it returns number "buzz"
"""
def test_number_divisible_by_3_and_5():
    result = fizzbuzz(15)
    assert result == "Fizzbuzz"