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
totalInicial = sum(valores)

desconto = 0 
if totalInicial > 500:
    desconto = totalInicial * 0.1

totalDesconto = totalInicial - desconto

print(f'Total antes do desconto: {totalInicial}')
print(f'Desconto aplicado: {desconto}')
print(f'Total com desconto: {totalDesconto}')



