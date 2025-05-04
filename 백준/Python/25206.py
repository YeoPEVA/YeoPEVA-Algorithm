score_check = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 
         'B0': 3.0, 'C+': 2.5, 'C0': 2.0,
         'D+': 1.5, 'D0': 1.0, 'F':0.0}

total_score = 0
total_credit = 0

for i in range(0,20):
    lecture, credit, score = input().split()
    if score == 'P':
        continue
    else:
        total_score += float(credit) * score_check[score]
        total_credit += float(credit)

print(total_score/total_credit)