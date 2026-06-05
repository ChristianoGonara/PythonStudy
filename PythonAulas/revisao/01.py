alunos=int(input('n alunos:'))
aprovados=0
for i in range(alunos):
    soma=0
    for j in range(3):
        nota=int(input(f'nota {j+1}: '))
        soma+=nota
    
    media= soma/3
    if media >=7:
        aprovados+=1
        print('aprovado')
    elif media>=5:
        print('recuperacao')
    else:
        print('reprovado')
    
print(f'n aprovados: {aprovados}')