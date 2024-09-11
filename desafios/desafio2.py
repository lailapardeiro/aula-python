# Desafio 2: Concatenar e Repetir
    # Repetir Strings
        # ● Crie um programa que receba uma palavra do usuário e um número inteiro. O programa deve imprimir a palavra repetida o número de vezes especificado.

palavra = input('Escreva a palavra: ')
numero = int(input('Escreva quantas repetições deseja: '))

repeticao = (palavra + ' ') * numero
print(repeticao)