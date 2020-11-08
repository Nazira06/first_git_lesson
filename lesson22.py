login = input("Введите Ваш логин: ")
password = input("Введите логин: ")
if login.lower() == "Nazira" and len(password) < 9 and "$"in password:
    print("Вы вошли в систему!")
    name = input()
    age = input()
    email = input()
    print(name.title(), age, email)
else:
    if login.lower() != "nazira":
        print("не правильный логин")
    if not len(password) < 9 or "$" in password:
        print("Пароли не подходят")
