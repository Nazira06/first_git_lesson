time = int(input())
breakfast = False
lunch = False
dinner = False
if 0<= time < 24:
    if 8 <= time < 12:
        breakfast = True
        print(f"завтрак!{breakfast}", lunch,dinner)
    elif 12 <= time < 16:
        breakfast = True
        lunch = True
        print(f"обед{lunch}",breakfast,dinner)
    elif 16 <= time < 22:
        breakfast = True
        lunch = True
        dinner = True
        print( f"ужин{dinner}", lunch,breakfast)
    else:
        print("мы не работаем")
else:
        print("вы с другой планеты")




