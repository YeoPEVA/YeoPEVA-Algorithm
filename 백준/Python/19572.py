# 1, 2 -> a
# 1, 3 -> b
# 2, 3 -> c 
d1, d2, d3 = map(int, input().split())
dSum = (d1+d2+d3) / 2 

a = dSum - d3 
b = dSum - d2
c = dSum - d1 

if a > 0 and b > 0 and c > 0:
    print(1)
    print(a, end='')
    print(b, end='')
    print(c, end='')
else:
    print(-1)