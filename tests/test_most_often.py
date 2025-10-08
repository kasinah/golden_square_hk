from lib.most_often import MostOften

def test_most_often():
    mo = MostOften([1, 2, 2, 3, 3, 3])
    assert mo.get_most_often() == 3
    mo.add_new(3)
    assert mo.get_most_often() == 3
   