def contar_letras(texto):
    i=0

    for c in texto:
        if ('a' <= c <='z') or ('A' <= c <= 'Z'):
            i +=1
    return i

print(contar_letras('abc123!'))