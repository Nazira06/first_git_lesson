student_list = ['Emir', 'Aijan', 'Nazira', 'Baizak', 'Zarina', 'Sultan' ]
current_list = []
i = 0
student_list_not = []
student_len = len(student_list)
come_in = 1
while come_in != "0":
    come_in = input("Введите имя студента:")
    if come_in not in current_list:#проверяем пришел ли студент на занятия
        if come_in in student_list:#проверяем есть ли студент в списке
            current_list.append(come_in) #добовляем студента
            print("студент пришел на занятия")
        else:
            print("Такого студента не существует в списке")
    else:
        print("Студент уже пришел")
current_list_not = student_list
while i < len(current_list):
    if current_list[i] in current_list_not:
        current_list_not.remove(current_list[i])
    i += 1
print('Список присутсвующих:', current_list)
print('Список отсутсвующих:', current_list_not)

