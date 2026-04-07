# ANÁLISE:
# O yield transforma a função em gerador:
# - execução é pausada
# - estado é preservado
# Diferente de funções normais que executam até o fim (run-to-completion),
# aqui temos controle cooperativo do fluxo.

def linha():
    for i in range(3):
        yield i


g = linha()

print(next(g))
print(next(g))
print(next(g))