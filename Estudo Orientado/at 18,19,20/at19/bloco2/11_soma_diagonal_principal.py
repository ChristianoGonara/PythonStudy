def soma_diagonal(matriz):
    soma=0
    for i in range(len(matriz)):
       soma+= matriz[i][i]
    print(soma)