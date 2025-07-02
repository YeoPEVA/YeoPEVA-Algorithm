t = int(input())

for _ in range(t):
    store_n = int(input())
    store_p = sorted(map(int,input().split()))
    # (가장 큰 좌표 - 가장 작은 좌표) * 2 
    print((store_p[-1] - store_p[0]) * 2)
