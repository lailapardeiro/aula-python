# Desafio 4: Manipulação de Listas
    # Adicionar e Remover Itens
        # ● Crie um programa que inicie com uma lista de frutas. O programa deve permitir que o usuário adicione uma nova fruta à lista e, em seguida, remova uma fruta existente.
            # ○ Frutas Iniciais: maça, banana, laranja
        # Para esse desafio utilize
            # ● append() função para adicionar item na lista
                # ○ lista.append(novo_item)
        # ● remove() função para remover item na lista
                # ○ lista.remove(item_remover)
        # ● Utilize if da seguinte maneira
                # ○ if item_remove in lista:
                # ○ Esse if tem o significado de = “Se o item que você quer remover existe na lista = True”


frutas = ['maça', 'banana', 'laranja']
print('Lista de frutas:', frutas)
fruta_nova = input('Digite a fruta que deseja adicionar: ')
frutas.append(fruta_nova)
print('Lista de frutas atualizada:', frutas)

fruta_removida = input('Digite a fruta que deseja remover: ')
if fruta_removida in frutas:
    frutas.remove(fruta_removida)
    print(frutas)
else:
    print('Essa fruta não está na lista, tente novamente!')
