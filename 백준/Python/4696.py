while True:
    a = float(input())
    if a == 0:
        break
    else:
        total = 1 + a + a**2 + a**3 + a**4
        print(f"{total:.2f}")