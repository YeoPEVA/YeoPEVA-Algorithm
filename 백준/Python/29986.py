n, h = map(int,input().split())
a = input().split()

count = 0 

for i in a:
    if h >= int(i):
        count += 1

print(count)