import sys
input = sys.stdin.readline

# 악보 갯수
a = int(input())
# 난이도  
b = list(map(int, input().split()))
# 질문의 개수
c = int(input())

d = [0] * c

# 악보 실수 횟수 계산 (미리해야..)
for i in range(1, c):
    if b[i] > b[i+1]:
        d[i] += 1
print(d)

# 질문에 따른 출력 

#for i in range(c):
#    x, y = map(int, input().split())
#    print(d[])