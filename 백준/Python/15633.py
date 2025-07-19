n = int(input())

result = 0
for i in range(1,n+1):
    if n % i == 0:
        result += i 

print(result * 5 - 24)