contador = 0 
while contador < 5:
    print(contador)
    contador += 1



import time
dia = 5

while dia > 0:
    print(dia)
    time.sleep(1)
    dia -=1 
print('Feliz ano Novo!')



contador = 2
while contador > 0:
    print('Feliz ano Novo!')
    time.sleep(1)
    contador -= 1 



senha_correta = '1234'
senha = ''
while senha != senha_correta:
    senha = input('Digite a senha: ')
print('Acesso permitido!')




bandeiras = {54: 'MasterCard', 53: 'Visa', 33: 'Elo', 22: 'Alelo'}
digito = None

while True:
    try:
        digito = int(input('Digite um número (ou digite -1 para sair): '))

        if digito == -1:
            print('Saindo do programa.')
            break
        if digito in bandeiras:
            print(f'A bandeira correspondente é {bandeiras[digito]}')
            break
        else:
            print('Número invalido. Tente novamente.')
    except ValueError as vr:
        print('Não foi digitado um valor inteiro! Tente novamente.')
    except Exception as e:
        print('Erro :: ', e)