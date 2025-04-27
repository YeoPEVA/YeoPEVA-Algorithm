input_string = input()

for i in input_string:
    if i.isupper() == True:
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')
