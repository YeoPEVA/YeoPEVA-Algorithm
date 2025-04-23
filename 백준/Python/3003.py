in_checker = list(map(int, input().split()))

checker = [1,1,2,2,2,8]

for i in range (len(checker)):
    print(checker[i] - in_checker[i],end=" ")
