note = list(map(int, input().split()))
 
if note == sorted(note):
    print('ascending')
elif note == sorted(note, reverse=True):
    print('descending')
else:
    print('mixed')