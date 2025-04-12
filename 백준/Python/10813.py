n, m = map(int, input().split())

# 바구니 N개 보유
# 바구니 1번부터 N번까지 번호가 매겨짐

# 처음 바구니 -> 바구니 번호의 번호를 가진 공이 들어있음
# 바구니 번호 2개 입력 (교환)
# 이후, 바구니에 어떤 공이 들어있는지 구하는 프로그램

result = list(range(1, n+1))
# print(result)

tmp = 0
for i in range(m):
    x, y = map(int, input().split())
    tmp = result[x-1]
    result[x-1] = result[y-1] 
    result[y-1] = tmp


for i in range(n):
    print(str(result[i]) + " ", end="")
