def manipular_string(texto):

    texto_maisculo = texto.upper()
    texto_minusculo = texto.lower()
    texto_caractere = len(texto)

    return (texto_maisculo, texto_minusculo, texto_caractere)



def main():
    palavra = input('Digite uma string para ser manipulada: ')
    
    resultado_maiusculo, resultado_minusculo, resultado_total_caractere  = manipular_string(palavra)

    print(f'Sua palavra em maíusculo: {resultado_maiusculo}')
    print(f'Sua palavra em minúsculo: {resultado_minusculo}')
    print(f'Sua palavra em resultado_total_caractere: {resultado_total_caractere}')


main()