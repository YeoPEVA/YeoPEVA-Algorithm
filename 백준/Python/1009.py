T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    # a에 대한 (a^n % 10) 반복 패턴 저장
    pattern = []
    mod = a % 10

    # 패턴 구하기
    current = mod
    while current not in pattern:
        pattern.append(current)
        current = (current * mod) % 10

    # b번째 수의 위치는 (b - 1) % len(pattern)
    result = pattern[(b - 1) % len(pattern)]

    # 0이면 10번 컴퓨터
    if result == 0:
        print(10)
    else:
        print(result)
