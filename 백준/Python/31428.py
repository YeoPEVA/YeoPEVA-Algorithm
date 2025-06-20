n = int(input())

cloud_track = 0
sw_track = 0
iot_track = 0
ai_track = 0

track_list = input().split()  

for t in track_list:
    if t == 'C':
        cloud_track += 1
    elif t == 'S':
        sw_track += 1
    elif t == 'I':
        iot_track += 1
    else:
        ai_track += 1

helloBit = input()

if helloBit == 'C':
    print(cloud_track)
elif helloBit == 'S':
    print(sw_track)
elif helloBit == 'I':
    print(iot_track)
else:
    print(ai_track)
