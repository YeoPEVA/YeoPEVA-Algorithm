price = int(input())
product_count = int(input())

result = 0 

for i in range(product_count):
    a,b = map(int, input().split())
    result += a * b 

if result == price:
    print("Yes")
else:
    print("No")