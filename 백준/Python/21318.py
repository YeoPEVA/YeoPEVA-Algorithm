import sys
input = sys.stdin.readline

# 악보 갯수
a = int(input())
# 난이도  
b = list(map(int, input().split()))
# 질문의 개수
c = int(input())

# 결과 (누적) 저장을 위한 리스트 초기화 진행 
# 악보 간의 실수 횟수 (누적)
d = [0] * int(a + 1)
tmp = 0

# 악보 실수 횟수 계산 (누적합 계산)
# tmp -> 현재까지 발견한 실수 횟수 저장 / 임시변수
for i in range(a-1):
    if b[i] > b[i+1]:
        tmp += 1
    d[i+1] = tmp
d[-1] = tmp

# print(d)

# 질문에 따른 출력 / 구간 사이에 발생한 실수 횟수 계산 
for i in range(c):
    x, y = map(int, input().split())
    print(d[y-1] - d[x-1])