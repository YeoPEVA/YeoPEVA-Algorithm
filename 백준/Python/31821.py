result = 0
n = int(input())
menu = [int(input()) for _ in range(n)]

m = int(input())
for _ in range(m):
    eatM = int(input())
    result += menu[eatM - 1]

print(result)