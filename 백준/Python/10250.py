t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    floor = n % h
    room_line = (n//h) + 1
    if floor == 0:
        floor = h
        room_line -= 1
    print(floor * 100 + room_line)