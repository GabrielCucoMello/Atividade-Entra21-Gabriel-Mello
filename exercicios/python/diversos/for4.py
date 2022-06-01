lol = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    ['@', '#', '*']
]

for i in lol:
    # print(i)
    for x in i:
        pass
        # print(x, end=' ')

print()
    
pao = [
    [10, 20, 30],
    [15, 1, 2],
    [50, 3, 5]
]

for a, b, c in pao:
    resultado = (a - b) * c
    print(a, b, c, resultado)

print()

cubo = [
    [10, 20, 30],
    [15, 1, 2],
    [50, 3, 5],
    [45, 12, 7],
    [100, 200, 300]
]

vtotal = 0
for l, a, p in cubo:
    print(l, a, p, 'O volume destes valores é:', (l * a * p))
    vtotal += (l * a * p)

allmult = [
    [10, 20, 30],
    [15, 1, 2],
    [50, 3, 5],
    [45, 12, 7],
    [100, 200, 300]
]
p0 = 1
p1 = 1
p2 = 1
for x in allmult:
    p0 *= x[0]
    p1 *= x[1]
    p2 *= x[2]
print(p0, p1, p2)