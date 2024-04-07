"""
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma 
das salas das lâmpadas, qual interruptor controla cada lâmpada?
"""

lista = [
    ("lâmpada1", "Interruptor1"),
    ("lâmpada2", "Interruptor2"),
    ("lâmpada3", "Interruptor3")
]
explorados = []
nao_visitados = []


for i in range(0, 2):
    if lista[i] not in explorados:
        explorados.append(lista[i])
nao_visitados.append(lista[-1])

print(lista)
# [('lâmpada1', 'Interruptor1'), ('lâmpada2', 'Interruptor2'), ('lâmpada3', 'Interruptor3')]
print(explorados)
# [('lâmpada1', 'Interruptor1'), ('lâmpada2', 'Interruptor2')]
print(nao_visitados)
# [('lâmpada3', 'Interruptor3')]
