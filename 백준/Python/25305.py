# input
# 응시자 수, 상을 받는 사람 
a,b = input().split()
a = int(a)
b = int(b)

person_score = list(map(int, input().split()))
person_score.sort(reverse=True)

# print(person_score)
print(person_score[b-1])