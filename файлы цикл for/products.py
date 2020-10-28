products = ['bread', 'meat', 'egg', 'cheese']
file1 = open('products.txt', 'w')
for product in products:
    file1.write(product+' \n')
file1.close()
file2 = open('products.txt')
var = file2.readlines()
print(var)