'''
Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho adicione quebra de linha, ao final.

Crie um laco de repetição recebendo uma condição que irá executar apenas números pares esses números devem percorrer até 1500.

Crie uma função de impressão após laco com a descrição parabéns você conseguiu!

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim do laço repetição!
'''

def contagemPulando():
    decoracao = "="*20

    # Função de Impressão
    print(decoracao, "CABEÇALHO", decoracao)

    # Laço de Repetição
    for c in range(0, 1501, 2):
        print(c)

    # Função Impressao

    print(f"Parabéns você conseguiu \n {decoracao} RODAPÉ {decoracao}")  


   