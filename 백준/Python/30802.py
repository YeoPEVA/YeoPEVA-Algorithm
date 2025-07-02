n = int(input())
tshirt_S = list(map(int, input().split()))
t, p = map(int, input().split())

# 티셔츠 묶음 (t장), 펜 묶음 (p개)

t_result = 0

for i in tshirt_S:
    # print(i)
    if i == 0:
        continue
    elif i <= t:
        t_result += 1
    elif i % t == 0:
        t_result += (i // t)
    else:
        t_result += (i // t) + 1

print(t_result)
print(n//p, n%p)