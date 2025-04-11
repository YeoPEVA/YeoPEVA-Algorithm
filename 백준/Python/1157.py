checkString = input()
checkString = checkString.upper()

dict = {}

for i in checkString:
    tmp = 0
    if i not in dict:
        dict[i] = tmp + 1
    else:
        tmp = dict[i]
        dict[i] = tmp + 1

result = [k for k, v in dict.items() if max(dict.values()) == v]

if(len(result) > 1):
    print("?")
else:
    print(result[0])
