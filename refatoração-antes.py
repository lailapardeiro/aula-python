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

# Código Original 

# Variáveis de Preço
p1 = 100
p2 = 200
p3 = 300 

t = p1 + p2 + p3

desc = 0 
if t > 500:
    desc = t * 0.1

r = t - desc

print('Total antes do desconto:', t)
print('Desconto aplicado:', desc)
print('Total com desconto:', r )






