n1 = int(input())
n2 = int(input())

if n1==n2 and n1<0:
    print("0")
else:
    if n1 > n2:
        n1, n2 = n2, n1
    
    soma = 0
    for i in range(n1, n2+1):
        if i > 0:
            soma += i

print(soma)
