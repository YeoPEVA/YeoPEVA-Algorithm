a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))

for i in range(0,10):
    count = 0
    for n in result:
        if i == int(n):
            count += 1
    print(count)
