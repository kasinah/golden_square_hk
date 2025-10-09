from lib.includesTodo import *

def test_check_ContainString_todo():
    incTodo = IncludesTodo("#TODO buy milk")
    assert incTodo.check_ContainString_todo() == True
      

    incTodo = IncludesTodo(1224764)
    assert incTodo.check_ContainString_todo() == "That was not a valid string!"


    incTodo = IncludesTodo("")
    assert incTodo.check_ContainString_todo() == "empty list"

    incTodo = IncludesTodo("drink tea")
    assert incTodo.check_ContainString_todo() == False

    incTodo = IncludesTodo("learn to test-drive my code #TODO")
    assert incTodo.check_ContainString_todo() == True

