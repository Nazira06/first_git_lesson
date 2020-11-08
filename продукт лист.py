import random

product_list = ['asus','acer','iphone','samsung','intel hd',
                'nvidia','adata','kingston','macbook','xiomi',
                'iMac','amd','apacer']

def register_params(login, password, check_password):
    register_list = []
    if password == check_password:
        global code
        code = random.sample([0,1,2,3,4,5,6,7,8,9,0], 4)
        register_list.append(login)
        register_list.append(password)

        return register_list
    else:
        return 'Пароли не совпадают'
user = register_params('Nazira', '123456', '123456')
username = user[0]
password = user[1]
print(username,password)

def aff(login,password):
    if  login == username and password == password:
        return "Вы вошли в систему"
    else:
        return "пароли не совпадают"
print (aff('Nazira', '123456'))
def write_to():
    file1 = open('product_list.txt','w')
    for product in product_list:
        file1.write(product + '\n')
write_to()

def sort_list():
   with open('product_list.txt', 'r') as file2:
       f2 = file2.readlines()
       for product in f2:
            product = product.strip()

            if product == 'asus' or product == 'acer' or product == 'macbook':
                file1 = open('computers.txt', 'a')
                file1.write(product + '\n')
            elif product == 'iphone' or product == 'samsung' or product == 'xiomi':
                file2 = open('phones.txt', 'a')
                file2.write(product + '\n')

            elif product == 'adata' or product == 'kingston' or product == 'apacer':
                file3 = open('hdd.txt', 'a')
                file3.write(product + '\n')

            elif product == 'intel hd' or product == 'amd' or product == 'nvidia':
                file4 = open('vid.txt', 'a')
                file4.write(product + '\n')

def code_params():
    global code
    code = random.sample([1,2,3,4,5,6,7,8,9], 4)
    return code
code_params()
print(code)
def activate(our_code, code):
    if our_code == code:
        print(True)
    else:
        print(False)
print('код пришедший на почту', code)

our_code = list(input("Введите код для активации аккаунта:"))
true_code = []
for line in code:
    true_code.append(str(line))
activate(our_code, true_code)

def open_file(filenume:str):
    with open(filenume) as f1:
        f1_read = f1.read()
        return f1.read()
def screen_input(user_input):
    if user_input == "phones":
        print(open_file('phones.txt'))
    elif user_input == "computers":
        print(open_file('computers.txt'))
    elif user_input == "videocards":
        print(open_file('vid.txt'))
    elif user_input == "hdd":
        print(open_file('hdd.txt'))
    else:
        print('Вы ввели неверную категорию товара')
screen_input('phones')









