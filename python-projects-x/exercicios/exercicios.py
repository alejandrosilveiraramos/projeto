import exercicio01
import exercicio02
import exercicio03
import exercicio04
import exercicio05
import exercicio06

# cabecalho
decorativo = "*" * 10
print(decorativo, " Bem vindo a lista de exercícios da GUIDOLOOPING ", decorativo)

i = "sim"
while i != "não":
    # escolha de func
    escolha = int(input(" \n - Escolha qual exercício você deseja executar: exercicio0"))

    if escolha == 1:
        exercicio01.parImpar()
    elif escolha == 2:
        exercicio02.felizDiaDoProgramador()
    elif escolha == 3:
        exercicio03.contador()
    elif escolha == 4:
        exercicio04.somaMenorMaiorDiferenteDez()
    elif escolha == 5:
        exercicio05.contagemRegressiva()
    elif escolha == 6:
        exercicio06.contagemPulando()
    else:
        print(" - Esse numero não existe, tente novamente.")
    i = str(input(" - Deseja escolher outra atividade? (sim) ou (não): \n"))
print("\n", decorativo * 3, "Finalizado", decorativo * 3)

