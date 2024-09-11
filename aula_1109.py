# Método de Busca Leitura sem o encoding="utf-8"
with open('aula-python/text/exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Método de Busca Leitura com o encoding="utf-8"
with open('aula-python/text/exemplo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Método de Busca Escrever
with open('aula-python/text/exemplo2.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Olá! ')
    arquivo.write('Mundooo!')

# Método de Acrescentar sem o \n
with open('aula-python/text/exemplo.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Texto Adicional')

# Método de Acrescentar com o \n
with open('aula-python/text/exemplo.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('\nTexto Adicional')

