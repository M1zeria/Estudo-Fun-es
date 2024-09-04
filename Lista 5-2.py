import math
pi = 3.14
def areaCirculo(r):
    areaCirculo = pi*r**2
    return areaCirculo

def perimetroCirculo(r):
    perimetroCirculo = 2*pi*r
    return perimetroCirculo

def perimetroTriangulo(a, b, c):
    perimetroTriangulo= a+b+c
    return perimetroTriangulo

def areaTriangulo(a, b, c):
    p = perimetroTriangulo(a, b, c)/2
    areaTriangulo = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return areaTriangulo

def areaRetangulo(a, b):
    areaRetangulo= a*b
    return areaRetangulo

def perimetroRetangulo(a, b):
    perimetroRetangulo= (a*2)+(b*2)
    return perimetroRetangulo

print("Escolha a figura para calcular a área:")
print("(1) circunferência")
print("(2) triângulo")
print("(3) retângulo")

figura = int(input(""))


if figura == 1:
    r= int(input("Informe o raio da circunferência:"))
    print(f"A área da circunferência é: {areaCirculo(r)}")
    print(f"O perímetro da circunferência é: {perimetroCirculo(r)}")

if figura == 2:
    a, b, c = input("Informe as medidas dos lados do triângulo: ").split()
    print(f"A área do triângulo é: {areaTriangulo(int(a), int(b), int(c)):.2f}")
    print(f"O perímetro do triângulo é: {perimetroTriangulo(int(a), int(b), int(c))}")

if figura == 3:
    a, b = input().split()
    print(f"A área do retângulo é: {areaRetangulo(int(a), int(b))}")
    print(f"O perímetro do retângulo é: {perimetroRetangulo(int(a), int(b))}")
