som_km = 10
wait = 2
paht = int(input("Путь:"))
cost = 40
wait_status = input("Водитель, введите статус ожидания:")
come_status = input("Введите ваш статус ожидания:")
i = 1
while come_status != 'True':
    cost = cost + wait
    i = i + 1
    come_status = input("Введите ваш статус ожидания:")
cost = cost + (paht * som_km)
print(cost)
