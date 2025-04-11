check = int(input())

# 소 정보 / 최소 횟수 
dict = {}
count = 0

for i in range(check):
    # 소 번호 및 위치 입력 
    a,b = map(int, input().split())

    # 소 번호가 dict 내에 없다면, 추가 
    if a not in dict:
        dict[a] = b
    # 소 번호가 있는 경우, 위치 값이 다른 경우 count 증가 
    else:
        if dict[a] != b:
            count += 1
            dict[a] = b
    # print("test #" + str(i) + " : " + str(dict))
print(count)


    
