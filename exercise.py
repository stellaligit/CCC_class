def fizz_buzz(integer):
    if integer % 3 == 0 and integer % 5 != 0:
        return "Fizz"
    elif integer % 5 == 0 and integer % 3 != 0:
        return "Buzz"
    elif integer % 3 == 0 and integer % 5 == 0:
        return "FizzBuzz"
    else:
        return integer


print(fizz_buzz(15))
