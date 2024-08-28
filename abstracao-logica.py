
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

