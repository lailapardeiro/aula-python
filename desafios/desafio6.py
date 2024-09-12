# Desafio 6: Manipulação de Dicionários/Objetos
    # Adicionar e Acessar Itens
        # ● Crie um dicionário que armazene informações sobre um livro (título, autor, ano). O programa deve permitir ao usuário atualizar o ano de publicação e imprimir a informação atualizada.

livro = {'titulo': 'Alice no País das Maravilhas', 'autor': 'Lewis Carroll', 'ano_publicacao': 1960}
print(livro)
novo_ano = input('Digite o ano atualizado: ')
livro['ano_publicacao'] = novo_ano
print(livro)