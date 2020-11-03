def count_vowels(txt):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in txt:
        if letter in vowels:
            count += 1
    return count
print(count_vowels('palm'))