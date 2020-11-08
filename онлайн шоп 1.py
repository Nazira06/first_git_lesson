products = {'gucci boots':10000,'channel':20000,'adidas boots':8000,
            'nike sport-suit':23000,'gucci sport-suit':24000,
            'Lonsdale suit':8000,'nike boots':9000,
            'dior chest':10000,'raben waist':15000,
            'wedding dress':50000,'socks':3000}

username = 'username'
password = 'pass12345'
def auth(login,password):
    if login == username and len(login) >= 8 and not password.isdigit() and not password.isalpha():
        return ["Вход выполнен!", login, password]
    else:
        return ["Введите правильные данные!", login, password]

print(auth('username','pass12345'))

def counter(money,price):
    if money >= price:
        money = money - price
        return money
    else:
        return "У вас недостаточно средств!"

def cart():
    cart_list = []
    for i in range(3):
        product = input("Введите товар: ")
        if product in products:
            cart_list.append(product)
    return cart_list

test_cart = cart()
def wallet(money):
    test_cart1 = []
    for i in test_cart:
        if money > products[i]:
            money = counter(money, products[i])
            test_cart1.append(i)
    return {"Моя прихоть":test_cart, "То что я смог купить":test_cart1,"Сдача":money}

print(wallet(50000))