a,b = input().split()
a = int(a)
b = int(b)

## 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6
## 2 + 3 + 3 + 3 + 4 
c = []

# 수열 제작 
for i in range(1, 1001):
    for j in range(i):
        c.append(i)
#print(c)

# 수열 계산 
# print(c[a-1:b])
result = sum(c[a-1:b])
print(result)