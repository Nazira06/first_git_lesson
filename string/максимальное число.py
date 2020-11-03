number = '123abvg4567'
list1 = []
for digit in number:
    if digit.isdigit():
        list1.append(int(digit))


print(max(list1))