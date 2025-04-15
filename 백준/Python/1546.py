# 시험 본 과목 갯수
n = int(input())

# 교과목 점수 입력
subject = [int(x) for x in input().split()]

# 최고점 확인 (max)
max_subject = max(subject)
result = 0

# 연산 -  점수/최고점 * 100 
for i in subject:
    tmp = i/max_subject * 100 
    result += tmp 

print(result/n)
