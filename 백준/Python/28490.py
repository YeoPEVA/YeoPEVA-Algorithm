n = int(input())

result = 0
for _ in range(n):
    a,b = map(int, input().split())
    
    if a*b > result:
        result = a*b
print(result)