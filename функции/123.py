#функции
def factorial(number):
    i = 1
    result = 1
    while i <= number:
        result = result * i
        i = i + 1
    print(result)
factorial(5)
factorial(6)
factorial(120)