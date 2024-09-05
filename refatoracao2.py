# Variáveis Globais
idade = int(input('Digite a idade desejada: '))

# Será validado a idade da persona para analisar sua categoria
def validar_idade(idade):
    mensagem_padrao = 'A pessoa é classificada como: '
    if idade < 0:
        return 'Essa por a caso já nasceu?'
    
    elif idade > 0 and idade <= 2:
        return mensagem_padrao + 'bebê!' 
    
    elif idade > 2 and idade < 13:
        return mensagem_padrao + 'criança!'

    elif idade >= 13 and idade < 18: 
        return mensagem_padrao + 'adolescente!'

    elif idade >= 18 and idade <= 60:
        return mensagem_padrao + 'adulto!'

    elif idade > 60 and idade <= 105:
        return mensagem_padrao + 'idoso!'
    
    else:
        return 'Alguém verificia se está vivo?!'

categoria_idade = validar_idade(idade)

print(categoria_idade)