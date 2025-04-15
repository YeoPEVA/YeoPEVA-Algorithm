# 바구니 - N
# 바구니 순서 변경 - M

# 1 2 3 4 5
# 2 1 3 4 5
# 2 1 4 3 5
# 3 4 1 2 5
# 3 4 1 2 5 

n, m = map(int, input().split())

result = []

# 바구니 생성 
for i in range(1, n+1):
    result.append(i)

# i, j 입력 (i에서 j까지의 범위를 역순으로 변경)
for i in range(m):
    i, j = map(int, input().split())
    # i ~ j 범위 리스트 tmp로 슬라이싱 
    tmp = result[i-1:j]
    # 슬라이싱한 tmp, reverse 활용을 통해 변경
    tmp.reverse()
    # tmp 리스트 저장 
    result[i-1:j] = tmp

for i in range(n):
    print(str(result[i]) + " ", end = '')