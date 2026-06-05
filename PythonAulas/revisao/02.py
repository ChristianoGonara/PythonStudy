n=int(input(' '))
lista=[]
while n != 0:
    lista.append(n)
    n=int(input(' '))

soma= sum(lista)
media= soma/len(lista)
maior= max(lista)
menor=min(lista)

print(f'soma: {soma}')
print(f'media: {media:.1f}')
print(f'maior: {maior}')
print(f'menor: {menor}')