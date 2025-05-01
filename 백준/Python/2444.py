size = int(input())

# 위쪽 (1 ~ N줄)
for i in range(1, size + 1):
    # 공백, 별 출력 
    spaces = ' ' * (size - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

# print()

# 아래쪽 (N+1 ~ 2N-1줄)
for i in range(size - 1, 0, -1):
    # 공백, 별 출력 
    spaces = ' ' * (size - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
