money = int(input("введите вашу сумму:"))
product_price = 3000
if money > product_price:
    result = money - product_price
    print('ваша сдача:,result')
elif money == product_price:
    print("спасибо за покупку")
else:
    print("у вас недостаточно средств")