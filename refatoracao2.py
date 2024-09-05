# O usuário irá colocar a idade desejada, o int ajuda a receber apenas números inteiros
idade = int(input('Digite a idade:'))
classificacao =  ' ' 
# Se a idade colocada for menor que 13 anos, é considearado criança
if idade < 13:
    classificacao = "criança"
# Se a idade colocada for igual ou maior que 13 e menor que 18 é considerado um adolescente
elif idade >= 13 and idade < 18: 
    classificacao = "adolescente"
# Se a idade colocada for igual ou maior que 18 e menor que 60 é considerado um adulto
elif idade >= 18 and idade < 60:
    classificacao = "adulto"
# Se a idade colocada for igual ou maior que 60 anos é considerado um idoso
else: 
    classificacao = 'idoso'

print(f'A pessoa é classificada como {classificacao}')