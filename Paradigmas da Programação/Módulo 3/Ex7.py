# ANÁLISE:
# Sem caso base, a recursão nunca termina.
# Cada chamada ocupa espaço na pilha.
# Isso leva ao erro:
# RecursionError (estouro da pilha)

def errado(n):
    return errado(n-1)


def correto(n):
    if n <= 0:  # caso base
        return
    print(n)
    correto(n-1)


correto(5)