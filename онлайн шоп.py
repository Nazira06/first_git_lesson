products = {'gucci boots':10000,'chanel':20000,'adidas boots':8000,
            'nike sport-suit':23000,'gucci sport-suit':24000,
            'Lonsdale suit':8000,'nike boots':9000,
            'dior chest':10000,'raben waist':15000,
            'wedding dress':500000
            }
username = 'Nazira'
password = 'naz2610'

def aff(login,password):
    if  login == username and password == password and len(login)<20 and not password.isdigit() and not password.isalpha():
        return "Вы вошли в систему"
    else:
        return "Вы ввели неверные данные"

print(aff('Nazira', 'naz2610'))

def counter(money,price):
    if money >= price:
        money = money - price
        return counter
    else:
        return "У вас не хватает денег"


def card():
    cart_lisd = []
    for i in range(2):
        product = input('Введите товар для покупки:')
        if product in products:
            cart_lisd.append(product)
    return cart_lisd

test_card = card()
def wallet(money):
    list_card = []
    for i in test_card:
        if money >= products[i]:
            money = counter(money,products[i])
            list_card.append(i)
    return {'Моя при хоть:': test_card, 'То что я смогла купить: ': list_card,'сдача:': money}
print(wallet(50000))




















