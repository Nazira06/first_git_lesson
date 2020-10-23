username=input("введите имя пользователя:")
len_username=len(username)
if len_username<20:
    print("продолжать регистрироваться дальше:")
else:
    print("введите имя заново")