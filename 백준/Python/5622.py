dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] 
in_string = input()

# 숫자 1을 거는데 2초 걸림 / 한 칸 옆 숫자 -> 1초씩 더 걸림
# UNUCIC -> 868242

result = 0

# 문자열 길이만큼 반복 
for i in range(len(in_string)):
    # dial 영문자 / 접근 
    for j in dial:
        if in_string[i] in j:
            # index 값 + 3 / (숫자 1 거는데 2초)
            result += dial.index(j) + 3 

print(result)