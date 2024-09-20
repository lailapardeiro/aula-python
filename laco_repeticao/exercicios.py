# Exercício 1

for i in range(11):
        print(i)


# Exercício 2

frutas = ['Banana', 'Uva', 'Laranja', 'Limão', 'Maça']
for indice, fruta in enumerate(frutas):
        print(f'Índice: {indice}, Valor: {fruta}')

# Exercício 3 

for par in range(0, 21, 2):
        print(par)

# Exercício 4

for impar in range(11):
        if impar % 2 == 0:
                continue
        print(impar)

for par in range(11):
        if par % 2 == 1:
                continue
        print(par)

# Exercício 5
soma = 0
numero = ''

while numero != 0:
        numero = int(input('Digite os número que deseja somar (digite 0 quando desejar que pare): '))
        soma += numero
print(f'A soma dos números digitados é igual a {soma}!')