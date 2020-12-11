with open('input.txt') as f:
    inputs = [int(x) for x in f.readlines()]

inputs.sort()
inputs.insert(0, 0)
inputs.append(inputs[-1] + 3)
ones = 0
threes = 0
for i in range(1, len(inputs)):
   diff = inputs[i] - inputs[i-1]
   ones += (diff == 1)
   threes += (diff == 3)
print(ones * threes)