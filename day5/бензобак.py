paht = 240
v = int(input("введите обьем бензина:"))#обьем бенз в данное вр
result = paht / 100
fuel = v - (result * 12)
if fuel > 1:
    print(f"вы доехали до места назначения у вас осталось:{round(fuel)} литр(a) бензина")
else:
    result = 100 / 12
    result = result * v
    print(f"у вас закончится бензин на {round(result)} километре")