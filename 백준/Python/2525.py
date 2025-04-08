# 시, 분 
h,m = map(int, input().split())
# 소요시간 (분)
c = int(input())

time_m = h*60 + m + c  

h = time_m / 60
# h = (time_m / 60) % 24 
# 위와 같이도 가능 (참고)
m = time_m % 60

if(h >= 24):
    h -= 24

print(int(h), m)