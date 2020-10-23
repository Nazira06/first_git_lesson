i = 1
number_list = []
while i <= 10:
    number_list.append(i)
    i += 1
prime_number = []
j = 0
while j < len(number_list):
    if number_list[j] % 2 ==0:
        prime_number.append(number_list[j])
    j += 1
print(prime_number)
print(number_list)



