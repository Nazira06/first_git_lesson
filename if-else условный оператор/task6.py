# вход в систему используя  ЛОГИЧЕСКОЕ И
loqin="username"
password="123456"
loqin1=input("введите имя пользователя:")
password1=input("введите пароль:")
if loqin1==loqin and password1==password:
    print("вы вошли в систему:")
else:
    print("не удается войти:")