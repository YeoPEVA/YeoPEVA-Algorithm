# 방학 
L = int(input())
# 국어 / 수학 (풀이)
A = int(input())
B = int(input())

# 하루 풀이 가능 횟수 (국어, 수학)
C = int(input())
D = int(input())

language_S = A // C 
math_S = B // D

if language_S > math_S:
    if A % C == 0:
        print(L - language_S)
    else:
        print(L  - language_S -1)
else:
    if B % D == 0:
        print(L - math_S)
    else:
        print(L - math_S -1)