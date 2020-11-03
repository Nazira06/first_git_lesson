def is_curzon(number):
    result1 = 2 ** number + 1
    result2 = 2 * number + 1
    if result1 % result2 == 0:
        return True
    else:
        return False
print(is_curzon(5))


