def coluna_maior_soma(matriz):
    maior_soma=0
    coluna_maior=0
    for coluna in range (len(matriz[0])):
        soma=0
        for linha in range(len(matriz)):
            soma += matriz[linha][coluna]
        if soma > maior_soma:
            maior_soma=soma
            coluna_maior=coluna

    print(coluna_maior)
    print(maior_soma)