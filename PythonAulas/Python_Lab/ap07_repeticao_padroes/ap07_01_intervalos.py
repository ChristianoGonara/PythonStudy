def classificar_numero(n):
    #tc: n = 16 -> 'multiplo de ambos'
    if n % 3 == 0 and n % 5 == 0: return "multiplo de ambos"
    if n % 3 == 0: return "multiplo de 3"
    if n % 5 == 0: return "multiplo de 5"
    return "nenhum"

def main():
    a=int(input('a: '))
    b=int(input('b: '))

    for i in range (a,b+1):
        print(f'\n numero {i}:')

        for j in range (1,i+1):
            print(f'{j} - {classificar_numero(j)}')
main()


#if n %3 ==0
#if n % 5 ==0
#if n % 3  and n %5 ==0