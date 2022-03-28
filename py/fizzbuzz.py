def multiplesOf(num, factor):
    # Is the number a multiple of the factor?
    return (num % factor == 0)

for i in range(100):
    if multiplesOf(i, 3) and multiplesOf(i, 5):
        print("FizzBuzz")
    elif multiplesOf(i, 3):
        print("Fizz")
    elif multiplesOf(i, 5):
        print("Buzz")
    else:
        print(i)