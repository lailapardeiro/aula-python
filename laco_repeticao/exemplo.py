lista_frutas = ['Maçã', 'Banana', 'Uva', 'Pera']

for fruta in lista_frutas:
    if(isinstance(fruta, int)): # se não for um valor inteiro, não quero continuar
        continue

    if(len(fruta) == 4):
        print(fruta)

import time
contador = 0 
while True:
    print(contador)
    if(contador == 12):
        break
    time.sleep(0.5)
    contador +=1



def saudacao():
    while True:
        try:
            nome = input('Qual é o seu nome? ')
            idade = int(input('Qual é a sua idade? '))

            print(f'Me chamo {nome} e tenho {idade} anos')
            break
        except ValueError:
            print('Foi digitado a idade incorretamente. Tente novamente!')

saudacao()