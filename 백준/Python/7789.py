# https://www.acmicpc.net/problem/7789

def is_prime_number(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

a, b = input().split()
phone_n = int(b+a)

if is_prime_number(int(a)) and is_prime_number(int(phone_n)):
    print("Yes")
else:
    print("No")