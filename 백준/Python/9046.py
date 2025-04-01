a = int(input())

# cipher input
for i in range(a):
    string = input()
    dic = {}
    # cipher check
    for chr in string.replace(" ", ""):
        if chr in dic:
            dic[chr] += 1
        else:
            dic[chr] = 1

    # 딕셔너리 내 최댓값
    count = max(dic.values())
    # 딕셔너리 내에서 값(v), 같은 키(k)들만 모아서 리스트 제작
    count_result = [k for k, v in dic.items() if v == count]

    # 리스트 길이로 확인 후 출력
    if len(count_result) > 1:
        print("?")
    else:
        print(count_result[0])