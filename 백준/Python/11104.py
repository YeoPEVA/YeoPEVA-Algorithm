n = int(input())

for i in range(0, n):
    a = input()
    # 앞 0 제거 / 최초 1부터 슬라이싱 진행 
    a = a[a.index('1'):]
    print(int(a,2))