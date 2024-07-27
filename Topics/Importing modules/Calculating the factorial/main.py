# don't modify this code or variable `x` may not be available
x = int(input())

# use factorial() here

def factorial(x):

    factorial = 1

    for i in range(1, x + 1):

        factorial = factorial * i

    return print(factorial)

factorial(x)