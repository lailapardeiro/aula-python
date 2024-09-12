# Desafio 7: Manipulação de Dicionários/Objetos
    # Pesquisar no Dicionário
        # ● Crie um dicionário onde as chaves são nomes de alunos e os valores são suas notas finais. O programa deve pedir ao usuário o nome de um aluno e exibir a nota desse aluno.
        # Para esse desafio utilize
            # ● Utilize if da seguinte maneira
                # ○ if aluno in notas:
                # ○ Esse if tem o significado de = “Se aluno que foi digitado existe na lista = True”

aluno = {'laila': 70, 'cauã': 57, 'lorena ': 70}

nome = input('Digite o aluno que deseja saber a nota: ')
if nome in aluno:
    print(f'A nota de {nome} é:', aluno[nome])


