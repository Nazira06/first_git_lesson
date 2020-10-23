
bmw = 20
merc = 18
fit= 9
fuel= int(input("Заправьте авто:"))
i = 0
while i < 3:
    auto = input("Введите наименование авто для тестирование:")
    result = 0
    final = 0
    paht = 240
    if auto == 'bmw':
        result = paht/100
        result = bmw * result
        final = fuel - result
        if final > 0:
            print(f"После поездки остаток:{final} литров")
        else:
            result = 100 // bmw
            result = result * fuel
            paht = paht - result
            print(f"Вам осталось ехать{paht}км")
    elif auto == "merc":
        result = paht / 100
        result = merc * result
        final = fuel - result
        if final > 0:
            print(f"после поездки остаток:{final} литров")
        else:
            result = 100 / merc
            result = result * fuel
            paht = paht - result
            print(f"Вам осталось ехать:{round(paht)}")
    elif auto == "fit":
            result = paht / 100
            result = fit * result
            final = fuel - result
            if final > 0:
                print(f"после поездки остаток:{final} литров")
            else:
                result = 100 / fit
                result = result * fuel
                paht = paht - result
                print(f"Вам осталось ехать:{round(paht)}")
    i = i + 1










