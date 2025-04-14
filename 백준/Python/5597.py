student = []

for i in range(28):
    x = int(input())
    student.append(x)

# 정렬
student_sort = sorted(student)

# 정렬 후 학생 번호 여부 체크 
result = []
for i in range(1,31):
    if i not in student_sort:
        result.append(i)

print(result[0])
print(result[1])

