def find_even_nums(number):
    even_list = []
    for i in range(1,number+1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list
print(find_even_nums(10))