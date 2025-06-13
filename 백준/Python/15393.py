t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    reward = 0
    
    if a == 0:
        pass
    elif a <= 1:
        reward += 500
    elif a <= 3:
        reward += 300
    elif a <= 6:
        reward += 200
    elif a <= 10:
        reward += 50
    elif a <= 15:
        reward += 30
    elif a <= 21:
        reward += 10

    if b == 0:
        pass
    elif b <= 1:
        reward += 512
    elif b <= 3:
        reward += 256
    elif b <= 7:
        reward += 128
    elif b <= 15:
        reward += 64
    elif b <= 31:
        reward += 32

    print(reward*10000)