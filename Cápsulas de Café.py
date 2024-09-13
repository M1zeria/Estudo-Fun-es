quantidadeTotal = 0
contador = 0
while contador != 7:
    quantidade = int(input())
    tamanho = str(input()).lower()

    if tamanho == "p":
        quantidadeTotal = quantidadeTotal+(quantidade*10)

    if tamanho == "g":
        quantidadeTotal = quantidadeTotal+(quantidade*16)
 
    contador += 1
print(quantidadeTotal)
print(f"{(quantidadeTotal/7)*2:.0f}")
