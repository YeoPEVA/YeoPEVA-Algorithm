while True:
    a, b, c = input().split()
    a, c = int(a), int(c) 

    if a == 0 and c == 0 and b == 'W':
        break

    if b == 'D':
        print(a+c)
    else:
        if (a-c < -200):
            print("Not allowed")
        else:
            print(a - c)