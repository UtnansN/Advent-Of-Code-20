import math

with open('input.txt') as f:
    inputs = f.read()

def binary_part(inStr, lowerTag, upperTag):
    return int(inStr.replace(lowerTag, '0').replace(upperTag, '1'), 2)

maxID = 0
MAX_ROWS = 128
rowCharLength = math.ceil(math.log(MAX_ROWS, 2))
for code in inputs.splitlines():
    row = binary_part(code[:rowCharLength], 'F', 'B')
    col = binary_part(code[rowCharLength:], 'L', 'R')
    passID = int(row * 8 + col)
    maxID = max(maxID, passID)
print(maxID)