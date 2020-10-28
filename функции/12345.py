username = 'user'
password = '12345678'
def login (login, check_password):
    if login == username and check_password == password:
        return login, check_password
    else:
        return 'Пароли не совпадают'
print (login('user', '12345678'))