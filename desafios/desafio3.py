# Desafio 3: Fatiar Strings
    # Extrair Nome do Meio
        # ● Dada uma string com o formato "Primeiro Nome Sobrenome", crie um programa que extraia e imprima apenas o nome do meio (ou seja, o sobrenome).
    # Para esse desafio utilize:
        # ● split() é um método de strings que divide a string em uma lista de substrings com base em um delimitador.
            # ○ texto = “Eu me chamo Leonardo”
            # ○ texto.split() # Saída: [‘Eu’, ‘me’, ‘chamo’, ‘Leonardo’]
        # ● len() é usada para obter o comprimento (ou número de itens) de um objeto.
            # ○ nome = “Leonardo”
            # ○ len(nome) # Saída: 8

nome = input('Digite seu nome completo: ')
sobrenome = nome.split()
if len(sobrenome) > 1:
    sobrenome = sobrenome[-1]

else:
    sobrenome = "Sobrenome não encontrado, tente novamente!"
print(f'Bem vindo, {sobrenome}!')