k = int(input())

n = 2 **k-1 
result = n*(n+1)//2
print(bin(result)[2:])