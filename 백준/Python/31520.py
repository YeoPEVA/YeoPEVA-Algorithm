s = input()
start = 1
chk = ''
while len(s) != len(chk):
    chk += str(start)
    if s[:len(chk)] != chk:
        print(-1)
        break
    start += 1
else:
    print(start - 1 if chk == s else -1)