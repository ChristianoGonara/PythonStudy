def linha_maior_soma(matriz):
    maior_soma=0
    linha_maior=0
    for i in range(len(matriz)):
        soma=0
        for j in range(len(matriz[i])):
            
            soma+= matriz[i][j]
            if soma >=maior_soma:
                maior_soma=soma
                linha_maior=i
    print(linha_maior)
    print(maior_soma)
            