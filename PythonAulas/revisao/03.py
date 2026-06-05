horas=int(input('horas: '))
temperatura=int(input('temperatura: '))
contador =0

while temperatura <=90 and contador<horas:
    if temperatura % 2 ==0:
        temperatura +=3
    else:
        temperatura-=1
    contador+=1

    if temperatura >90:
        print('Alerta!')

print(f'quantas horas : {contador}')
print(f'temperatura final = {temperatura}')
