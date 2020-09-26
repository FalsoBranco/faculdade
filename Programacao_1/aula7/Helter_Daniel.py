"""
Questão 01 (1.0 ponto): Algoritmo é um conjunto finito de instruções destinados a resolver um problema mediante a um conjunto finito de dados. O que será impresso pelo algoritmo abaixo?

indice = (1, 0, 3, 2, 5, 4)
semana = ('seg', 'ter', 'qua', 'dom','sex', 'sab')
for i in indice:
    print(semana[i])

# ('ter','seg','dom','qua','sab','sex')   
 """


"""
Questão 02 (1.0 ponto): Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão e imprima o resultado de D: 
D = (R+S)/2
Onde:
R = (A+B)**2
S = (B+C)**2
"""


def foo(numbers: list) -> int:
    A, B, C = numbers
    R = (A + B)**2
    S = (B + C)**2
    D = (R + S) / 2
    return D


entrada = [int(input(f"{x}° valor: ")) for x in range(1, 4)]

print(foo(entrada))


"""
Questão 03 (1.0 ponto): Descreva o que acontece em cada linha do algoritmo abaixo:

nota2 : float(input("Entre com a nota 1")) # nota 1 recebera um numero digitado pelo usuário, fazendo um cast para float
nota1 : float(input("Entre com a nota 1")) # nota 2 recebera um numero digitado pelo usuário, fazendo um cast para float

media = (nota1+ nota2) / 2 # Calculara a media das duas notas

print("A média é : " , media) # escrevera a string junto a media

if media >= 7: # se a media for maior ou igual a 7 execultara a ação abaixo, senão, pula para proxima contição 
    print("Aprovado!!!") # Escrevera aprovado
elif media >= 3: # se a media for maior ou igual a 3 execultara a ação abaixo
    print("Final") # Escrevera Final
else: # se a media nao entrar em nenhumas das condições acima.
    print("Game Over") # Escrevera Game Over
"""


"""
Questão 04 (1 ponto): Construa um algoritmo, dado três valores, A, B, C, verificar se eles podem ser classificados como triângulo: equilátero, isósceles ou qualquer. Os valores são inteiros e positivos.

"""


def triangle(sides: list) -> str:

    if len(set(sides)) == 1:
        return 'triangulo equilatero'
    elif len(set(sides)) == 2:
        return 'tringulo Isosceles'

    return "Outro"


entrada = [int(input(f"{x}° valor: ")) for x in range(3)]
print(triangle(entrada))


"""
Questão 05 (1 ponto): Construir um algoritmo capaz de ler um número e
imprimir se este número é positivo, negativo ou zero.
"""


def check_PosNeg() -> str:
    number = int(input("Digite um numero: "))
    if number > 0:
        return "Positivo"
    elif number < 0:
        return "Negativo"

    return "Zero"


print(check_PosNeg())

"""
Questão 06 (2 pontos): Dado uma matriz MAT de 4 X 5 elementos, faça um
algoritmo para somar os elementos de cada linha gerando o vetor SOMALINHA.
Em seguida, somar os elementos do vetor SOMALINHA na variável TOTAL que
deve ser impresso no final.

    0  1  2  3  4
 +--+--+--+--+--+ +--+
0 | 1| 0| 2|-1| 3| --> | 5|
1 | 4| 3| 2| 1| 0| --> |10| SOMA
2 | 1|-2| 3| 4| 5| --> |11| LINHA
3 | 8| 5| 1| 3| 2| --> |19|
 +--+--+--+--+--+      +--+
                       +--+
                       |45| TOTAL
                       +--+

"""
MAT = [
    [1, 0, 2, -1, 3],
    [4, 3, 2, 1, 0],
    [1, -2, 3, 4, 5],
    [8, 5, 1, 3, 2],
]

# Maneira resumida: total = sum([sum(x) for x in MAT])
total = 0
for row in MAT:
    soma_linha = 0
    for col in row:
        soma_linha += col
    total += soma_linha
print(total)
