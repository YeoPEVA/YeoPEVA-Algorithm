n = int(input())

for _ in range(n):
    a = int(input())
    tmp = 1
    for i in range(1, a+1):
        tmp *= i
    print(tmp % 10)