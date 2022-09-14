'''
Crie uma variável com valor fixo esta variável deve conter um numero que não interfira na decisão de um índice.

Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho adicione quebra de linha, ao final.

Crie um laco de repetição, este laço deve solicitar ao usuário para digitar um número por 3 vezes.

Dentro do laço, crie a capacidade de soma entre esses números digitados, eles devem ser atributos de soma.

Crie uma função de impressão usando máscara de substituição e imprima de forma descritiva a soma desses números.

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim do laço de repetição.

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho início estrutura de decisão adicione quebra de linha, ao final.

Crie uma estrutura de condição falando se a soma desses números é maior que 10, menor que 10, igual a dez, diferente de 10.

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim da estrutura de decisão.
'''

# Variaveis

num = 0
poli = '=' * 10
soma = 0

# Impressao Cabeçalho

print(f'{poli} CABEÇALHO {poli}\n')

# Estrutura de repetição

for c in range(0, 3):
    numero = int(input('Digite um número: '))
    soma += numero

# Funçao Impressao Somas

print('A soma dos números digitados é {}'.format(soma))


print(f'{poli} RODAPE {poli}\n')

# Impressao Cabeçalho

print(f'{poli} CABEÇALHO {poli}\n')

# Estrutura de Condição

validador = True

if soma  > 10:
    print('Maior que dez: {}'.format(validador))

if soma < 10:
    print('Menor que dez: {}'.format(validador))

if soma == 10:
    print('Igual que dez: {}'.format(validador))

if soma != 10:
    print('Diferente que dez: {}'.format(validador))      

# Impressao Rodape

print(f'{poli} RODAPE {poli}\n')