# x,y 
x = int(input())
y = int(input())

if x >= 1 and y >= 1:
    print("1")
elif x <= -1 and y >= 1:
    print("2")
elif x <= -1 and y <= -1:
    print("3")
else:
    print("4")

