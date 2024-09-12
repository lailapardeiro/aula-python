# Desafio 5: Trabalhar com Tuplas
    # Criar e Acessar Tuplas
        # ● Crie uma tupla contendo três coordenadas (x, y, z). O programa deve permitir ao usuário alterar a coordenada y e exibir a tupla atualizada.

tupla = (10,20,30)
print(tupla)
novo_indice = int(input('Digite o novo valor de y: '))
tupla = (tupla[0], novo_indice, tupla[2])
print(tupla)