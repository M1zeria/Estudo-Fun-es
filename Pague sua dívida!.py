dividaTotal = int(input())
mensal = int(input())

if dividaTotal <= mensal:
    print(f"(antes) {dividaTotal}")
    print(f"(depois) 0")
else:  
    while dividaTotal > mensal:
        print(f"(antes) {dividaTotal}")
        print(f"(depois) {dividaTotal-mensal}")
        dividaTotal = dividaTotal-mensal
        if dividaTotal == mensal:
            print(f"(antes) {dividaTotal}")
            print(f"(depois) 0")

