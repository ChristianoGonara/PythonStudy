#Objetivo: Classificar o produto final.
#classificcar produti fonal
#tc 4,3 #12 -> 'par, medio'

def analisar_produto(p):
    paridade='par' if p % 2 == 0 else 'impar '

    if p <=10:
        faixa = 'pequeno'
    elif p <=20:
        faixa = 'medio'

    else:
        faixa='grande'

    return f'{paridade}, {faixa}'

def main ():
    l=int(input('Digite a linha : '))
    c=int(input('Digite a coluna: '))
    produto = l*c
    classificacao=analisar_produto(produto)
    print(f'linha {l} e coluna {c} -> produto = {produto} -> {classificacao}')
main()