def extrair_vogais(texto):
    vogais= 'aeiouAEIOU'
    resultado = ''

    for c in texto:
        if c in vogais:
            resultado +=c
            
    return resultado
    
print(extrair_vogais('computador'))