n = int(input())
count = 0

for i in range(0,n):
    checker = 0
    word_in = input()
    
    for j in range(len(word_in)-1):
        # 현재 문자 -> 뒤 문자와 동일 -> pass 
        if word_in[j] == word_in[j+1]:
            pass 
        # 현재 문자 -> 뒤 문자와 동일 x, 이후 문자열 내 해당 문자 존재시
        # 그룹 문자열 X 
        elif word_in[j] in word_in[j+1:]:
            checker = 1 
            break    
    if(checker != 1):
        count += 1

print(count)