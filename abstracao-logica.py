
# Atividade sobre abstração lógica 
numero=input('Digite um número: ')
def verificarNumero(x):
    numero=int(x)
    if numero > 0:
        return print('O número é positivo!')
    elif numero < 0: 
        return print('O número é negativo!')
    else:
        return print('O número é zero!')
verificarNumero(numero)

# Atividade usando and e or
a=2
b=6
c=3
operacaoAnd = a == b and c*a == b
print(operacaoAnd)
operacaoOr = a == b or c * a == b
print(operacaoOr)
