n, m = map(int, input().split())

# 바구니 N개 보유
# 바구니 1번부터 N번까지 번호가 매겨짐
# 처음 바구니 -> 공 X / 바구니에는 공 1개만 넣을 수 있음
# 바구니 M번 공을 넣음
# 이후, 바구니에 어떤 공이 들어있는지 구하는 프로그램

result = [0 for i in range(n)]

for i in range(m):
    x, y, z = map(int, input().split())
    for j in range(x-1, y):
        if(result[j] != z):
            result[j] = z

for i in range(n):
    print(str(result[i]) + " ", end="")
