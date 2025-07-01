# 고정비용, 가변비용, 판매가 
a, b, c = map(int, input().split())
count = 1

if b >= c:
    print(-1)
else: 
    print(a//(c-b)+1)
    #while True:
    #    if(a + (b * count) < (c * count)):
    #        print(count)
    #        break
    #    else:
    #        count += 1 
