def fizzbuzz(num):
    if num % 3 == 0 and num %5 == 0:
        return "Fizzbuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num