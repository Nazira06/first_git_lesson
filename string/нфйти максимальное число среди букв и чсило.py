number = '123abvg4567'
list1 = []
for digit in number:
    if digit.isdigit():
        list1.append(digit)
print(list1)
print(number)
print(max(list1))