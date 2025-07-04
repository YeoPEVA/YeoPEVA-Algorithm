n = int(input())
n_list = map(int, input().split())

result = 0

for i in n_list:
    if i < 2:
        continue  # 0과 1은 소수가 아님
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):  # 제곱근까지만 확인해도 됨
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        result += 1

print(result)
