n = int(input())
x = 1
y = 2
z = 3

produto = x*y*z
triangular = False

while produto <= n:
    if produto ==n:
        triangular = True
        break
    x += 1
    y += 1
    z += 1
    produto = x * y * z
if triangular:
    print(f"{x} * {y} * {z} = {n}\nVerdadeiro")
else:
    print("Falso")
