username_list = []
password_list = []
i = 0
while i < 5:
    username = input("ВВедите имя пользователя:")
    password = input("Введите пароль:")
    username_list.append(username)
    password_list.append(password)
    print(f'пользователь под номером{i} зарегистрирован')
    i = i +1
print(username_list)
print(password_list)