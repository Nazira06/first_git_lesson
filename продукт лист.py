import random

product_list = ['asus','acer','iphone','samsung','intel hd',
                'nvidia','adata','kingston','macbook','xiomi',
                'iMac','amd','apacer']

def register_params(login, password, check_password):
    register_list = []
    if password == check_password:
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
   with open('product.txt', 'r') as file2:
       f2 = file2.readlines()
       for product in f2:
            if product == 'asus' or product == 'acer' or product == 'macbook':
                file1 = open('computers.txt', 'w')
                file1.write(product)
            elif product == 'iphone' or product == 'samsung' or product == 'xiomi':
                file2 = open('phones.txt', 'w')
                file2.write(product)

            elif product == 'adata' or product == 'kingston' or product == 'apacer':
                file3 = open('hdd.txt', 'w')
                file3.write(product)

            elif product == 'intel hd' or product == 'amd' or product == 'nvidia':
                file4 = open('vid.txt', 'w')
                file4.write(product)
print(sort_list())


