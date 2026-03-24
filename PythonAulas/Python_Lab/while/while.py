# 1 a 10
def ex01():
    i=0
    while i <=10:
        print (i)
        i+= 1


#10 a 1
def ex02():
    i=10
    while i >=1:
        print (i)
        i-=1


#soma de 1 ate n
def ex03():
    n=int(input('Digito: '))
    i=1
    soma = 0

    while i <=n:
        soma +=i
        i+=1
    print(soma)


# tabuada de um numero
def ex04():
    n=int(input('Digito: '))
    i = 1

    while i <=10:
        resultado = n * i
        print (f'{n} x {i} = {resultado}')
        i+=1


#media 5 notas
def ex05():
    soma = 0
    i=1
    while i <=5:
        nota = float(input(f'{i} nota: '))
        soma += nota
        i+=1
    media = soma / 5
    print(f'media das 5 notas: {media:.2f}')


#contador pares e impar
def ex06():
    i=1
    n=''
    par = 0
    impar = 0

    while i <=10:
        n=int(input(f'{i} numero: '))

        if n % 2 == 0:
            par +=1
        else:
            impar +=1
        i+=1

    print(f'{par} pares')
    print(f'{impar} impares')
          

#menor e maior valor informado  | ler 8 inteiros
def ex07():
    n=int(input('1 numero: '))
    maior=n
    menor=n
    i=2

    while i <=8:
        n=int(input(f'{i} numero: '))

        if n > maior:
            maior = n
        if n < menor:
            menor = n
        i+=1

    print(f'maior: {maior}')
    print(f'menor {menor}')

ex07()