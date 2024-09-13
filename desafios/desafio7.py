# Desafio 7: Manipulação de Dicionários/Objetos
    # Pesquisar no Dicionário
        # ● Crie um dicionário onde as chaves são nomes de alunos e os valores são suas notas finais. O programa deve pedir ao usuário o nome de um aluno e exibir a nota desse aluno.
        # Para esse desafio utilize
            # ● Utilize if da seguinte maneira
                # ○ if aluno in notas:
                # ○ Esse if tem o significado de = “Se aluno que foi digitado existe na lista = True”

alunos = {"laila": 80, "caua": 95, "lorena": 100}

def recuperarNotaAluno(aluno):
    if aluno in alunos:
        print(f"O aluno {aluno} está com nota: {alunos[aluno]}")
    else:
        print("Aluno não encontrado! Tente novamente")

        operacao = input("Deseja tentar novamente? (S/N) ")
        if operacao.upper() == "S":
            main()
        elif operacao.upper() == "N":
            print("Programa finalizado!")
        else:
            print("Operação não reconhecida! O programa irá finalizar!")
        

def main():
    aluno = input("Digite o nome do aluno que deseja consultar a nota: ")
    recuperarNotaAluno(aluno)

main()   