#распорядок дня
day_plan = ['qo to shop', 'clean house', 'cook smth', 'eat', 'walk']
plun_len = len(day_plan)
i = 0
while i < plun_len:
    action = input("введите действие:")
    if action in day_plan:
        act_index = day_plan.index(action)
        if act_index == 0:
            day_plan.remove(action)
            i = i + 1
        else:
            print("не тороптресь!")
    else:
        print("Вы это не планировали!")

    print(f'оставшиешя дела {day_plan}')

