# 28/08/2024
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

# 29/08/2024
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

if diaFesta == dia:
    print('Ana está fazendo as compras no dia da festa!')
else:
    print('Ana está fazendo a compra adiantada')

if(pedidoMinimoPizza > pedidoPizza):
    if(pedidoMinimoPizza == pedidoPizza):
        print('Ana comprou o mínimo pedido de pizzas!')
    print('Ana não comprou o suficiente!')
else:
    print('Ana comprou mais pizzas do que o esperado!')


if(pedidoMinimoBebida < pedidoBebida):
    print('Ana comprou mais bebidas que o necessário!')
elif(pedidoMinimoBebida == pedidoBebida):
    print('Ana comprou a quantidade necessária de bebidas!')
else:
    print('Não comprou as bebidas suficientes!')


if(pedidoMinimoBolo < pedidoBolo):
    print('Ana excedeu a compra de bolos!')
elif(pedidoMinimoBolo == pedidoBolo):
    print('Ana comprou mais bolos que o necessário!')
else: 
    print('Ana comprou os bolos!')

if(pedidoMinimoDoce > pedidoDoce):
    print('Ana não comprou doces suficientes!')
elif(pedidoMinimoDoce < pedidoMinimoDoce):
    print('Ana comprou mais doces que o imaginado!')
else: 
    print('Ana comprou a quantidade necessária de doces!')