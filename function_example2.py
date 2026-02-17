def add_numbers(a, b, c=0):
    """

    Adds 2 or 3 numbers
    :param a: first number
    :param b: second number
    :param c: third number
    :return: result of addition of two/three numbers
    """
    return a + b + c

print(add_numbers(1,2,3))
print(add_numbers(5,7))

# a function can call itself (recursive function)
def factorial (n):
    """
    Calculates the factorial of a number
    :param n: the n
    :return: factorial result
    """

result = 1
for i in range(1, n + 1):
    result *= i
return result


def rec_factorial(n):
    if n == 1:
        return 1
    return n * rec_factorial(n - 1)

print(factorial(6))
print(rec_factorial(6))