n = int(input())
while n != 0:
    ultimoN = n % 10
    resto = (n - ultimoN)/10

    resultado = ultimoN * 5 + resto
    if resultado % 7 == 0:
        print("S")
    else:
        print("N")
    n = int(input())
