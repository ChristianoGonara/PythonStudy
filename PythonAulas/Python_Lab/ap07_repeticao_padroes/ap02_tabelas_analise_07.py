def analisar_paridade(n):
    if n % 2 ==0: return 'par'
    return "impar"

def verificar_limite(n):
    if n >20:
        return "maior que 20"
    return "ate 20"

def classificar_faixa(n):
    if n<=10:
        return "pequeno"
    elif n <=20:
        return "medio"
    else:
        return "grande"
    
def main():
    linhas=int(input('linhas: '))
    colunas=int(input('colunas: '))

    for i in range (1,linhas+1):
        for j in range (1,colunas+1):
            produto = i*j

            paridade=analisar_paridade(produto)
            limite=verificar_limite(produto)
            faixa=classificar_faixa(produto)

            print(f'linha {i} e coluna {j} -> produto = {produto} -> {paridade}, {limite}, {faixa}')
main()