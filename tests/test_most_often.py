from lib.most_often import MostOften

def test_most_often():
    mo = MostOften([1, 2, 2, 3, 3, 3])
    assert mo.get_most_often() == 3
    mo.add_new(3)
    assert mo.get_most_often() == 3     
    mo.add_new(2)
    assert mo.get_most_often() == 3     
    mo = MostOften(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])
    assert mo.get_most_often() == 'banana'
    mo.add_new('apple')
    assert mo.get_most_often() == 'no clear winner'
    mo.add_new('apple')
    assert mo.get_most_often() == 'apple'       
    mo = MostOften(['cat', 'dog', 'fish'])
    assert mo.get_most_often() == 'no clear winner' 
    mo.add_new('cat')
    assert mo.get_most_often() == 'cat'
    mo.add_new('dog')
    assert mo.get_most_often() == 'no clear winner'


   