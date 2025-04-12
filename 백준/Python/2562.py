dict = {}

for i in range(0,9):
    tmp = int(input())
    dict[i] = tmp 


sorted_dict = sorted(dict.items(), key=lambda item:item[1])

result = sorted_dict[-1]
print(result[1])
print(result[0]+1)