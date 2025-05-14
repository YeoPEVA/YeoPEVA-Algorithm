table = []

# 9*9 테이블
for _ in range(9):
    row = list(map(int, input().split()))
    table.append(row)

max_value = 0
max_row, max_col = 0, 0

# 순회 / max 값 및 row, col 위치 파악 
for row in range(9):
    for col in range(9):
        if max_value <= table[row][col]:
            max_row, max_col = row + 1, col + 1
            max_value = table[row][col]

print(max_value)
print(max_row, max_col)