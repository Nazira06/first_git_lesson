user_db = ''
password_db = ''
def register(usernume, password, repead_password):
    if password == repead_password:
        user_db == usernume
        password_db == password
        return user_db,password_db
    else:
        return 'Пароли не совпадают'
    print(register('nazira', '261026', '261026'))





