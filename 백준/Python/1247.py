from sys import stdin

for _ in range(3):
    n = int(input())
    s_li = [int(input()) for i in range(n)]

    if sum(s_li) == 0:
        print("0")
    elif sum(s_li) > 0:
        print("+")
    else:
        print("-")