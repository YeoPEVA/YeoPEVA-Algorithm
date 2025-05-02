str_in = input()
str_set = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in str_set:
    str_in = str_in.replace(i, "*")

print(len(str_in))