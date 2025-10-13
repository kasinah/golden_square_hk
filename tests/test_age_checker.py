from lib.age_checker import *
"""
        Given the user is less than 16 years old
        then it return message "Access denied" 
        AND Their current age and the required age (16)
"""
def test_age_is_under_16():
    res = age_checker("2024-01-01")
    assert res == "Access denied"

"""
        Given the user is more than 16 years old
        then it return message "Access granted" 
"""
def test_age_is_above_16():
    res = age_checker("2009-01-01")
    assert res == "Access granted"


"""
        Given the user is more than 16 years old
        then it return message "Access granted" 
"""
