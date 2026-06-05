def verificar_matriz_quadrada(matriz):
    if len(matriz) == len(matriz[0]):
        print('eh quadrada')
    else:
        print('nao eh quadrada')