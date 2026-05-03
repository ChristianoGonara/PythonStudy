
n=int(input('Digite a quantidade de termos: '))
atual=0
proximo=1
contador = 0
soma = 0

while contador <n:
    print(atual) #atual

    soma = atual + proximo
    atual = proximo
    contador +=1
    