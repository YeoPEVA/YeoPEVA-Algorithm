while True:
    try:
        h, p = map(int, input().split())
        print('%.2f'%round(h/p, 2))
    except EOFError:
        break