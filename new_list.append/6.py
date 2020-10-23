numbers = [1, 'red', 2, 'yellow', 'qreen', 3, 5.7, 10.9, [10.5, 1]]
int_list = []
float_list = []
str_list = []
i = 0
while i < len(numbers):
    if isinstance(numbers[i], str):
        str_list.append(numbers[i])
    elif isinstance(numbers[i],float):
        float_list.append(numbers[i])
    else:
        int_list.append(numbers[i])
    i += 1
print(f'общий список {numbers}')
print(f'список содержащий строки {str_list}')
print(f' список содержащий числа {int_list}')
print(f' список содержащий дробные числа {float_list}')