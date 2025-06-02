t = int(input())

for i in range(0, t):
    n = int(input())
    round = "Round 1"

    if n <= 25:
        round = "World Finals"
    elif n <= 1000:
        round = "Round 3"
    elif n <= 4500:
        round = "Round 2"
    
    print(f"Case #{i+1}: {round}")