def verificar_elementos_iguais(matriz):
    for i in range(len(matriz)):
        iguais=True
        for j in range (len(matriz[i])):
            if matriz[i][j] != matriz[i][0]:
                iguais=False
        if iguais:
            print(f'linha {i}: sao iguais')
        else:
            print(f'linha {i}: nao sao iguais')
        