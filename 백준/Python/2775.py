t = int(input())  

# 아파트 배열 초기화 (0층 ~ 14층 /  1호 ~ 14호)
apt = [[0] * 15 for _ in range(15)]

# 0층 초기화 / i호에는 i명이 산다
for i in range(1, 15):
    apt[0][i] = i

# 나머지 층 채우기 / a층 b호에는 아래층 1호부터 b호까지의 합
for i in range(1, 15):  # 1층부터 14층
    for j in range(1, 15):  # 1호부터 14호
        apt[i][j] = apt[i][j-1] + apt[i-1][j]

for _ in range(t):
    k = int(input())  # 층 수
    n = int(input())  # 호 수
    print(apt[k][n])