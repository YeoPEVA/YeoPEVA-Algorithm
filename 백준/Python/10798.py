# 입력 및 문자열 길이 저장 
string = []
string_len = []

for i in range(5):
    word = input()
    string.append(word)
    string_len.append(len(word))

#print(string)
#print(string_len)

# 가장 긴 길이의 문자열 기준으로 반복문 진행 
for i in range(max(string_len)):
    # 입력 - 다섯줄 / 5번 반복 
    for j in range(5):
        # i 값이 문자열 길이보다 작은 경우에만 출력 
        if i < string_len[j]:
            print(string[j][i], end="")