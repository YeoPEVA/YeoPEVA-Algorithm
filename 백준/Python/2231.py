n = int(input())

result = 0

for i in range(1, n+1):
    checker = list(map(int, str(i)))
    result = sum(checker) + i 
    
    if result == n:
        print(i)
        break
    if i == n:
        print(0)