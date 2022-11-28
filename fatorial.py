def fatorial(valor):
    contador = valor
    fatorial = 1
    while contador >= 1:
        fatorial *= contador
        contador -=1
    return fatorial
    
    
#print(f"O fatorial de {valor} é {fatorial}")


fatorial(6)
         