#Fatorial
# input , se contador <=n; 
#resultado = resultado * i 
#contador +=1
n= int (input('Digite um numero: '))
i=1
resultado=1

while i <=n:
    resultado = resultado * i
    i +=1

print(f'fatorial:{resultado}')