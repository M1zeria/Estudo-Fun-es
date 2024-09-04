def calcS (n):
    s = 0
    for i in range(n):
        s = s+1/n
        n -= 1
    return s

n = int(input())

print(calcS(n))
