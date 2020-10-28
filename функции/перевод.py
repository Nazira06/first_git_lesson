def translator():
    print(f"Выберите правильный ответ как переводится кошка:, {['cat', 'apple']}")
    answer = input("Введите ответ:")
    if answer == 'cat':
        print("Вы ответили правильно!")
    else:
        print("неправильно!")
translator()