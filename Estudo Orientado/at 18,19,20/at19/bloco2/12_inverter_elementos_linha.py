def inverter_elementos_linha(matriz):
    for i in range(len(matriz)):

        for j in range(len(matriz[i])-1,-1,-1):
            print(matriz[i][j])
