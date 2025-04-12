
x, y = map(int, input().split())
check = list(map(int, input().split()))

for i in check:
    if(i < y):
        print(str(i) + " ", end='')

