def factorial(i):
    if i == 0 or i== 1:
        return 1
    else:
        return factorial(i-1) * i 

a = int(input())
print(factorial(a))