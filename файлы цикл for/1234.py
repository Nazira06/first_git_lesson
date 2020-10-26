file1 = open('phones.txt', 'a')
for i in range(5):
    phone_number = int(input())
    file1.write(str(phone_number)+'\n')
file1.close()
file2 = open('phones.txt', 'r')
phone_number_list = file2.readlines()
print(phone_number_list)
file2.close()