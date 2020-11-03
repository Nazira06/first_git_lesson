def settify(number_list):
    number_list.sort()
    empty_list = []
    for number in number_list:
        if number not in empty_list:
            empty_list.append(number)
    return empty_list
print(settify([1,2,3,4,4,5,5,6,6,7,7,]))
print(set(([1,1,2,2,3,3,4,5,6,7])))