"""
Faça com que a função FirstReverse (str) pegue o parâmetro str que está sendo passado e 
retorne a string na ordem inversa. Por exemplo: se a string de entrada for 
"Hello World and Coders", seu programa deve retornar a string sredoC dna dlroW olleH .
"""

def FirstReverse(string):
    string = string[::-1]
    return string


print(FirstReverse("Hello World and Coders"))
