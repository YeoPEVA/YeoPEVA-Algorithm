result = []

# 연산 후 리스트 추가
for i in range(10):
    x = int(input())
    tmp = x%42
    # 연산 결과가 result 내에 있다면 추가 X
    if tmp not in result:
        result.append(tmp)

print(len(result))