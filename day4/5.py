boots = 3000
wear = 4500
scarf = 900
money = int(input("введите вашу сумму:"))
product = input("введите товар для покупки(boots wear scaf):")
if product == 'boots':
    if money >= boots:
        print('спасибо за покупку')
    else:
        print('у вас недостаточно средств')
elif product == 'wear':
    if money >= wear:
        print("спасибо за покупку")
    else:
        print("у вас недостаточно средств")


