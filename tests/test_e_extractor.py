
from lib.e_extractor import*
"""
Given that the string has no e in it
Then it returns same string 
"""

def test_e_extractor_no_e():
    res = e_extractor("abc")
    assert res == "abc"