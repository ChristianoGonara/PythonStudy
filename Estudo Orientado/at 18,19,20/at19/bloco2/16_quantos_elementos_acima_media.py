def acima_media_matriz(matriz):
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma+=matriz[i][j]

    total=len(matriz)*len(matriz[0])
    media=soma/total
    contador=0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > media:
                contador+=1

    print(contador)



