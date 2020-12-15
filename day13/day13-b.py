import math
with open('input.txt') as f:
    f.readline()
    buses = [time for time in f.readline().strip().split(',')]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    _, x, _ = egcd(a, m)
    return x % m

offsets = [(int(num), (int(num) - (offset % int(num))) % int(num)) for offset, num in enumerate(buses) if num != 'x']
M = int(math.prod(m for m, _ in offsets))
M_div = [int(M / m) for m, _ in offsets]
inv = [modinv(M_div[i], v[0]) for i, v in enumerate(offsets)]
total = sum(a * M_div[i] * inv[i] for i, (_, a) in enumerate(offsets))
print(int(total) % M)