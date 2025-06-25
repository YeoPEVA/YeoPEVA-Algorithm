while True:
    inlist = list(map(int, input().split()))
    if inlist[0] == inlist[1] == inlist[2] == 0:
        break
    inlist.sort()

    if inlist[2]**2 == inlist[0]**2 + inlist[1]**2:
        print("right")
    else:
        print("wrong")