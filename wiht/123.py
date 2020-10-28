def write_to(filename:str,text:str):
    with open(f"{filename}.txt",'w') as file1:
        file1.write(text)
write_to('players', 'Hello, Hi')