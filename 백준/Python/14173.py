# 입력
x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

min_x = min(x1_1, x1_2)
max_x = max(x2_1, x2_2)
min_y = min(y1_1, y1_2)
max_y = max(y2_1, y2_2)

side = max(max_x - min_x, max_y - min_y)

# 최소 면적 출력
print(side * side)
