string = 'irjflkjuhrfjd'
if string.istitle() and len(string) < 10:
    string = string.lower()
    print(string)
elif not string.istitle() and len(string) < 10:
    string = string.upper()
    print(string)
elif len(string) > 10:
    string = string.capitalize()
    print(string)


