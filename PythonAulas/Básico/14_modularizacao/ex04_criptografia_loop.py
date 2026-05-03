def criptografar(texto):
    resultado = ''
    for c in texto:
        if c == 'z':
            resultado +='a'
        else:
            resultado +=chr(ord(c)+1)

    return resultado

while True:
    palavra=input('Digite o texto: ')
    if palavra == 'fim':
        break

    print(criptografar(palavra))