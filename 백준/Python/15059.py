meal_c, meal_b, meal_p = map(int, input().split())
meal_cw, meal_bw, meal_pw = map(int, input().split())

result = 0 

if meal_cw > meal_c:
    result += meal_cw - meal_c

if meal_bw > meal_b:
    result += meal_bw - meal_b

if meal_pw > meal_p:
    result += meal_pw - meal_p

print(result)