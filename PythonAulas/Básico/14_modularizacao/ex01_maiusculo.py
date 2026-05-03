def para_maiusculo(texto):
    resultado = ''
    for c in texto:
        codigo=ord(c)

        if 97<= codigo <=122:
            resultado +=chr(codigo-32)
        else:
            resultado +=c
            
    return resultado
    
print(para_maiusculo('casa'))