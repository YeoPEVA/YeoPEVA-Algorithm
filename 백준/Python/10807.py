x = int(input())
check = list(map(int, input().split()))
y = int(input())

count = 0
for i in range (x):
    if(check[i] == y):
        count += 1

print(count)