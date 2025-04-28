input_str = list(input())
input_reverse = list(reversed(input_str))
# 입력 받은 문자열 리스트로 변환
# 입력 리스트 reversed를 통해 뒤집은 결과로 list로 묶음 

# 리스트 비교 / 동일시 -> 팰린드롬
if input_str == input_reverse:
    print(1)
else:
    print(0)