def calcular(operacao, numero1, numero2):
    if operacao == "+":
        soma = numero1 + numero2
        return soma 
    elif operacao == '-':
        subtracao = numero1 - numero2 
        return subtracao
    elif operacao == '*':
        multiplicacao = numero1 * numero2
        return multiplicacao
    elif operacao == '/':
        if numero2 == 0:
            return 'Não é possível realizar divisão com zero!'
        divisao = numero1 / numero2
        return divisao


def main():
    lista_operacoes = ['+', '-', '*', '/']
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    operacao = input('Digite a operação: ')

    if operacao not in lista_operacoes:
        print("A operação digitada não existe!")
        novamente = input(' Deseja tentar novamente? (S/N) ').upper()

        if novamente.upper() == "S":
            main()
        elif novamente.upper() == "N":
            print("Programa finalizado!")



    resultado = calcular(operacao, numero1, numero2)

    if isinstance(resultado, str):
        print(resultado)
    else: 
        print(f'Resultado {numero1} {operacao} {numero2} = {resultado:.2f}')

main()
