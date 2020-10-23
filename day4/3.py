loqin="nazira"#наш логин
password="123456"#
phone="0556121317"
email="nazira@com"#наша электронная почта
chek_input=input("phone or email:")#выбираем что вводить
if chek_input=='phone':
    phone_chek = int(input("введите телефон:"))
    password_chek=input("введите пароль:")
    if phone_chek==phone and password_chek==password:
        print("вы вошли в систему")
    else:
        print("Вы ввели неверные данные")
elif chek_input=='email':
    email_chek=input("введите E-Mail:")#вводим эл.почту
    password_chek=input("введитее пароль:")
    if email_chek==email and password_chek==password:
        print("вы вошли в систему")
    else:
        print('вы ввели неверные данные')

