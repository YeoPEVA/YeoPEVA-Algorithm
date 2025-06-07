bus, time = map(int, input().split())

bus_list = []

for i in range(bus):
    bus_start, bus_time = map(int, input().split())

    if (bus_start + bus_time) <= time:
        bus_list.append(bus_start)

if len(bus_list) == 0:
    print(-1)
else:
    print(max(bus_list)) 