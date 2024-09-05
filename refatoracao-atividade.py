idade = 25 

categoria = 'indefinida'
if idade < 13:
    categoria = 'criança'
elif idade >= 13 and idade < 18: 
    categoria = 'adolescente'
elif idade > 18 and idade < 60:
    categoria = 'adulto'
else: 
    categoria = 'idoso'

print('A pessoa é classificada como> ', categoria)