criteria = int(input())
mySpeed = int(input())
fine = 0

pr = f'You are speeding and your fine is ${fine}.'

if mySpeed <= criteria:
    print("Congratulations, you are within the speed limit!")
else:
    if (mySpeed - criteria <= 20):
        fine = 100
    elif (mySpeed - criteria <= 30):
        fine = 270
    else:
        fine = 500
    pr = f'You are speeding and your fine is ${fine}.'
    print(pr)
