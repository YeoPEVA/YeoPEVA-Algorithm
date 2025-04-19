t = int(input())

for i in range(t):
    r, s_in = input().split()
    r = int(r)
    s_in = list(s_in)
    for j in range(len(s_in)):
        print(str(s_in[j]) * r, end='')
    print()
