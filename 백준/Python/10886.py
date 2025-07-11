n = int(input())

result = 0
for _ in range(n):
    a = int(input())
    if a == 1:
        result += 1

if result >= n/2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")