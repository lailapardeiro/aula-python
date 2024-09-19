

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    operacao = input('Você deseja saber a temperatura em Celsius ou Fahrenheit? (C/F)')
    if operacao.upper() == "C":
        temperatura_celsius = float(input('Digite a temperatura em Celsius: '))
        temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
        print(f'A temperatura de {temperatura_celsius:.2f}°C equivale a {temperatura_fahrenheit:.2f}°F.')
    elif operacao.upper() == "F":
        temperatura_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
        temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
        print(f'A temperatura de {temperatura_fahrenheit:.2f}°F equivale a {temperatura_celsius:.2f}°C.')
    else:
        print("Operação não reconhecida! O programa irá finalizar!")

    novamente = input("Deseja tentar novamente? (S/N) ")
    if novamente.upper() == "S":
        main()
    elif novamente.upper() == "N":
        print("Programa finalizado!")
    else:
        print("Operação não reconhecida! O programa irá finalizar!")


main()
















