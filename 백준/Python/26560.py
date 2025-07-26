a = int(input())

for _ in range(a):
    b = input()
    if(b[-1:] == "."):
        print(b)
    else:
        print(b + ".")