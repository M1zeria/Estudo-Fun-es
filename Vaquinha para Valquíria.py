BvalorTotal = 0
contador = 1

AValor = float(input())
if AValor < 0:
    print("Insira os valores das doacoes:")
    print("Total arrecadado: 0.00")
    print("Valor medio da doacao: 0.00")
else:
    while True:
        Bvalor = float(input())
        if Bvalor < 0:
            break
        BvalorTotal = BvalorTotal + Bvalor
        contador += 1
    print("Insira os valores das doacoes:")
    print(f"Total arrecadado: {BvalorTotal+AValor:.2f}")
    print(f"Valor medio da doacao: {(BvalorTotal+AValor)/contador:.2f}")

