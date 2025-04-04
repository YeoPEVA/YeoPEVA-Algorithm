# input 
A,B,C,M = map(int, input().split())

# 피로도 - A
# 일 처리도 - B
# 휴식시 줄어드는 피로도 - C
# 피로도 최대치 - M 
# 하루에 최대 얼마나 많은 일을 할 수 있는지 출력 

# 5 3 2 10 -> 24 

# 피로도 - die
# 최대 일 - max_work
die = 0
max_work = 0

# 하루 24시간 반복 
for i in range(24):
    # 피로도가 최대치보다 큰 경우, -> 0 / 일 못함.
    if die > M:
        print(0)
    else:
        # die + A 결과, 최대치보다 작거나, 같다면
        # 피로도 증가 및 작업량 증가  
        if die + A <= M:
            die += A 
            max_work += B 
        # 그 외 경우, 휴식 
        else:
            # 휴식으로 피로도가 줄어든 경우 
            # 피로도 C만큼 감소한 결과가 0이상이면 감소 
            if die - C >= 0:
                die -= C
            # 휴식으로 피로도가 음수인 경우 -> 피로도 0
            else:
                die = 0 

print(max_work)

