
def parImpar():
    # Variaveis Numero e Divisao
    num = int(input('Digite um número: '))
    
    divisao = num % 2

    #  Função Impressão
    print('O resto da divisão de {} é {}'.format(num, divisao))
    
    # Estrutura de Condição
    if divisao == 0:
        print('É par')
    else:
        print('É impar')