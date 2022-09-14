'''
Crie uma variável do tipo inteiro recebendo dados.
Crie uma variável fazendo o cálculo do resto da divisão, usando máscara de substituição e realize a atribuição do valor.
Logo em seguida crie uma estrutura de condição onde irá imprimir no terminal se o cálculo da divisão e impar ou par.

'''

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
