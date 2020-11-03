number = input()

if number.startswith('996'):
    number = '+' +number
    print(number)
elif number.startswith('+996'):
    print(number)
elif not number.startswith('+996') and not number.startswith('0') and len(number) == 9:
    number = '+996' + number
    print(number)
else:
    print('!Введите телефон в правильном формате')