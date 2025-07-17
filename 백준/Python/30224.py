a = int(input())

a_7_str = '7' in str(a)
a_7_div = a % 7 == 0

if not a_7_str and not a_7_div:
    print(0)
elif not a_7_str and a_7_div:
    print(1)
elif a_7_str and not a_7_div:
    print(2)
else:
    print(3)