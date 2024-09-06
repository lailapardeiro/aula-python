texto = 'Olá, Mundo!'

# Fatiar do início até um índice específico
print(texto[:5]) # Saída: 'Olá, '

# Fatiar a partir de um índice específico até o final
print(texto[6:]) # Saída: 'undo!'

# Fatiar do início até o final, com um passo específico
print(texto[::2]) # Saída: 'Oá ud!'

# Fatiar com início e fim específicos
print(texto[4:9]) # Saída: ' Mund'

# Fatiar com passo negativo para inverter uma subtring
print(texto[::-1]) # Saída: '!odnuM ,álO"



frutas = ['maça', 'banana', 'laranja']
print('Lista de frutas:', frutas)

frutas.append('uva')
print('Lista de frutas atualizada:', frutas)

print('Primeira fruta:', frutas[0])
print('Segunda fruta:', frutas[3])

frutas.remove(frutas[2])
print(frutas)



pessoa = {"nome": "Ana", "idade": 30}
print('Pessoa:', pessoa)

print('Nome:', pessoa['nome'])

pessoa['cidade'] = 'São Paulo'
print('Pessoa atualizada:', pessoa)



pessoa = {'nome': 'Brenda', 'idade': 26, 'filhos': {'nome': 'Catarina', 'idade': 6}}
print(pessoa)

print(pessoa['nome'])

print(pessoa['filhos'])

print(pessoa['filhos']['nome'])

pessoaB = pessoa['filhos']
print(pessoa)

del pessoa['filhos']
print(pessoa)




lista_pessoas = []

pessoa = {'nome': 'Ana', 'idade': 32}
lista_pessoas.append(pessoa)
print(lista_pessoas)

pessoa = {'nome': 'Brenda', 'idade': 26}
lista_pessoas.append(pessoa)
print(lista_pessoas)

pessoa = {'nome': 'Fernanda', 'idade': 48}
lista_pessoas.append(pessoa)
print(lista_pessoas)

ana = lista_pessoas[0]
print(ana)



# x = 10, y = 30, z = 20
tupla = (10,20)
print(tupla)
tupla = (tupla[0], 30, tupla[1])
print(tupla)
# x = 10, y = 30, z = 30
print(tupla)
novo_indice = 20 
tupla = (tupla[0], novo_indice, tupla[2])
print(tupla)



lista = [1, 2, 2, 3, 4, 4]
# O set é usado para remover dados repetidos e deixar os elementos como únicos
conjunto = set(lista) 
print(conjunto)



a = {1 , 2, 3 }
b = {3, 4, 5}
print(a - b) # diferença apenas do primeiro valor



conjunto = {1, 2, 3, 4, 5}
# in = se existe, se tem
print(3 in conjunto)
print(6 in conjunto)