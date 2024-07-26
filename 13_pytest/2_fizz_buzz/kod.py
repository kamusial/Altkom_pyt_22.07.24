def fizzbuzz(i):
    if i != 0:
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        if i % 3 == 0:
            return 'Fizz'
        elif i % 5 == 0:
            return 'Buzz'
        return str(i)
    else:
        return None

