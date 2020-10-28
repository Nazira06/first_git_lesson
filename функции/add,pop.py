list1 = [1,2,3,4,5,6,7,8]
def chanqe_list(mode, number):
   if mode == 'add':
       list1.append(number)
   elif mode == 'pop' and number in list1:
       list1.pop(number)
   else:
       print('Вы ввели неверный мод!')
chanqe_list('add',10)
chanqe_list('pop',2)

print(list1)