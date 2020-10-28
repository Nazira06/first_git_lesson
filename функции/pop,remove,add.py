list1 = [1,2,3,4,5,6,7,8]
def chanqe_list(mode, number):
   if mode == 'add':
       list1.append(number)
   elif mode == 'remove' and number in list1:
       list1.remove(number)
   elif mode == 'pop':
       if number >= len(list1):
           print('Вы ввели слишком большое число')
       else:
        list1.pop(number)
   else:
       print('Вы ввели неверный мод!')
chanqe_list('add',10)
chanqe_list('remove',7)
chanqe_list('pop',9)
print(list1)