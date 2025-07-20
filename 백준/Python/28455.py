n = int(input())

levels = [int(input()) for _ in range(n)]

# 레벨 높은 순으로 정렬
levels.sort(reverse=True)

# 최대 42개까지만 
top_levels = levels[:42]

# 레벨합 
result2 = sum(top_levels)  
# 능력치 합
result = 0                 

for userLevel in top_levels:
    if userLevel >= 250:
        result += 5
    elif userLevel >= 200:
        result += 4
    elif userLevel >= 140:
        result += 3
    elif userLevel >= 100:
        result += 2
    elif userLevel >= 60:
        result += 1

print(result2, result)
