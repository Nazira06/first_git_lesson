def factorial(number):
    i = 1
    result = 1
    while i <= number:
        result = result * i
        i = i + 1
    return result
print(factorial(5))

