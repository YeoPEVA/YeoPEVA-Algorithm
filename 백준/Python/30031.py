n = int(input())
answer = 0

for _ in range(n):
    w, h = map(int, input().split())
    if w == 136:
        answer += 1000
    elif w == 142:
        answer += 5000
    elif w == 148:
        answer += 10000
    else:
        answer += 50000
print(answer)