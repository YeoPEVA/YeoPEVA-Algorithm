a = int(input())

for i in range(a):
    checker = list(map(int, input().split()))
    checker.sort(reverse=True)
    print(checker[2])
