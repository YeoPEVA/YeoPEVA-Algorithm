a = int(input())
check = list(map(int, input().split()))
check.sort()

print(str(check[0]) + " " +str(check[a-1]))