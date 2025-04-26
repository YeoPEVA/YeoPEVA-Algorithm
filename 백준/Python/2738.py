n, m = map(int, input().split())

a_check = [[0]*m for _ in range(n)]
b_check = [[0]*m for _ in range(n)]
# result = [[0]*m for _ in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        a_check[i][j] = a[j]

for i in range(n):
    b = list(map(int, input().split()))
    for j in range(m):
        b_check[i][j] = b[j]

for i in range(n):
    for j in range(m):
        print(int(a_check[i][j]) + int(b_check[i][j]), end=" ")
        # result[i][j] += a_check[i][j]
        # result[i][j] += b_check[i][j]
    print()

# print(result)