"""
Atividade
● Suba ao GitHub o código da forma que receber
● Melhore o código com funções que podem ser reaproveitadas 
● Melhore a legibilidade do código
● Atualize o GitHub com o código refatorado
Dicas
● Teste o Código Antes: Verifique se o código esteja funcional antes de iniciar a refatoração.
● Reveja o Código: Analise o código para identificar áreas que precisam de refatoração.
● Teste Após Refatorar: Certifique-se de que o código ainda funciona conforme esperado após a refatoração.
● Vocês tem total autonomia de refatorar o código da forma que quiserem, ajustar, implementar mais funções, etc.
"""


# Código Refatorado

# Váriaveis de Preço
valores = [100, 200, 300]

# totalInicial é a soma dos valores da lista acima.
total_inicial = sum(valores) 

print(f'Preço Total: {total_inicial}') 

# SE totalInicial for maior que 500, aplica um desconto de 10%
if total_inicial > 500:
# O total da compra é o totalInicial menos o desconto.
    total_desconto = total_inicial - (total_inicial * 0.1) 
    print(f'Total com desconto: {total_desconto}')
else:
    diferenca = 500 - total_inicial
    print(f'Faltou {diferenca} para o desconto ser aplicado! Deseha incluir mais produtos?')







