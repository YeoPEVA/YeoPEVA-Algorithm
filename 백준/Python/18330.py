n = int(input())
# 다음 달 사용 / 휘발유 양 
k = int(input())
# 주유 카드에 남은 할당량 
k += 60

result = 0

if k >= n:
    result = 1500 * n
else:
    result = 1500 * (k)
    result += 3000 * (n-k)
print(result)