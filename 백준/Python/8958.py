a = int(input())

for _ in range(a):
    ox_result = list(input())
    score = 0
    result = 0

    for i in ox_result:
        if i == 'O':
            score += 1 
            result += score
        else:
            score = 0
    print(result)