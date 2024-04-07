"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de 
Fibonacci e retorne uma mensagem avisando se o número 
informado pertence ou não a sequência.
"""


def fibonnaci(n):
    a, b = 0, 1
    steps = []
    for i in range(n):
        steps.append(a)
        a, b = b, a + b
    if n not in steps:
        return f'Este número não faz parte da sequência'
    return steps


print(fibonnaci(10))  # output: Este número não faz parte da sequência
print(fibonnaci(8))  # output: [0, 1, 1, 2, 3, 5, 8, 13]
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
print(fibonnaci(21))
