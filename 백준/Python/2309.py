
# input
sum = 0
person = []
for i in range(9):
    a = int(input())
    person.append(a)
    sum += a

# sort
person.sort()
# print(person)

# brute force
for i in range(len(person)):
    for j in range(i+1, len(person)):
        if sum - person[i] - person[j] == 100:
            for z in range(len(person)):
                if z == i or z == j:
                    pass
                else:
                    print(person[z])
            exit(0)