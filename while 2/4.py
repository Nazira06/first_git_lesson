score_list = []
score = 1
while score !=0:
    score = int(input("Введите оценк ребенка:"))
    if 0 < score <= 5:
        score_list.append(score)
        if score == 5:
            print("Молодец!")
        elif score == 4:
            print("Хорошо!")
        elif score == 3:
            print("Старайся лучше!")
        elif score == 2:
            print("Получишь ремнем!")
        elif score == 1:
            print("Месяц без компьютера!")
    else:
        print("Вы ввели неправильную оценку!")
print(score_list)
summary = sum(score_list)
print(summary/len(score_list))