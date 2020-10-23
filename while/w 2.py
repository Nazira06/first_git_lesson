user_name = 'Nazira'
password = '123456'
i = 0
while i < 5:
    loqin = input("Введите имя пользователя:")
    chek_password = input("Введите пароль:")
    if loqin == user_name and chek_password == password:
        print("Вы вошли в систему!")
        break
    else:
        print("Вы ввели неверные данные!")
        i = i + 1

