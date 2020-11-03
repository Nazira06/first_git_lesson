#Программа имеет список и выводит список из 3 элементов:первого,третьего и второго с конца
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
list2.append(list1[0])
list2.append(list1[2])

list_len = len(list1)
list2.append(list1[list_len - 2])
print(list2)