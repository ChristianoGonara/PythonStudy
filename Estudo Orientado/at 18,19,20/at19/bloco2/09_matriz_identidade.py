#matriz identidade exemplo
#1 0 0
#0 1 0
#0 0 1

n=3
matriz=[]

for i in range(n):
    linha=[]
    for j in range(n):
        if i ==j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
print(matriz)