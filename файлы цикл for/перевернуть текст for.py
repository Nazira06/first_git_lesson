def name_shuffle(txt):
    txt = 'Donald Trump'
    txt = txt.split()
    txt.reverse()
    result = ''
    for line in txt:
        result = result + ' ' +line
    return result
print(name_shuffle("Donald Trump"))

