import math
with open('input.txt') as f:
    earliest_time = int(f.readline())
    buses = [int(time) for time in f.readline().split(',') if time != 'x']

waiting_times = [math.ceil(earliest_time / time) * time - earliest_time for time in buses]
idx = 0
for i in range(len(waiting_times)):
    if waiting_times[i] <= waiting_times[idx]:
        idx = i
print(waiting_times[idx] * buses[idx])