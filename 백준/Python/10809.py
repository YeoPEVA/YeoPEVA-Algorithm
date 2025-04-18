a = input()
count = 0
result = [-1] * 26

for i in range (len(a)):
    # -1 / 이미 등장한 알벳의 경우 패스 
    # ascii / 98 (a) / 인덱스 계산
    if result[ord(a[i]) - 97] != -1:
        continue
    else:
        result[ord(a[i]) - 97] = i 

for i in result:
    print(i, end = ' ')