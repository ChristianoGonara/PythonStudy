def classificar_multiplo(n):
    """
    tc1: 3 -> 'multiplo de 3'
    tc3: 15 -> 'multiplo de ambos'
    """
    
    if n % 3 == 0 and n % 5 == 0:
        return 'multiplo de ambos'
    elif n % 3 == 0:
        return 'multiplo de ambos'
    elif n % 5 == 0:
        return 'multiplo de 5'
    return 'nenhum'

def main ():
    a=int(input('A: '))
    b=int(input('B: '))

    for i in range (a,b+1):
        print(f'\nnumero {i}: ')
        for j in range (1,i+1):
            print(f'{j} - {classificar_multiplo(j)}')
main()

