n, m = input().split()

n = str(n)
m = int(m)
result = ''

while len(result) < len(n) * int(n):
    result += n

print(result[:m])