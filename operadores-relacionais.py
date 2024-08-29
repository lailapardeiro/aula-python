# 29/08/2024
# Utilização de Operadores Relacionais
a = 5 
b = 3 

# Igualdade
resultado = a == b
print(resultado)

# Diferença
resultado = a != b
print(resultado)

# Maior que (>)
resultado = a > b
print(resultado)

# Menor que (<)
resultado = a < b
print(resultado)

# Maior ou igual (>=)
resultado = a >= b
print(resultado)

# Menor ou igual (<=)
resultado = a <= b 
print(resultado)

# Exercício 

# Declarando variáveis

dia = int(input('Qual o dia de hoje? '))
pedidoPizza = int(input('Quantas pizzas comprou? '))
pedidoBebida = int(input('Quantas bebidas comprou? '))
pedidoBolo = int(input('Quantos bolos comprou? '))
pedidoDoce = int(input('Quantos doces comprou? '))

diaFesta = 26
pedidoMinimoPizza = 10
pedidoMinimoBebida = 12
pedidoMinimoBolo = 5
pedidoMinimoDoce = 600

if diaFesta == (dia):
    print('Ana está fazendo as compras no dia da festa!')
else:
    print('Ana está fazendo a compra adiantada')

if(pedidoMinimoPizza) >= pedidoPizza:
    print('Ana não comprou pizzas suficientes!')

if(pedidoMinimoBebida) < pedidoBebida:
    print('Ana comprou mais bebidas que o necessário!')

if(pedidoMinimoBolo) <= pedidoBolo:
    print('Ana excedeu a compra de bolos!')

if(pedidoMinimoDoce) > pedidoDoce:
    print('Ana não comprou doces suficientes!')