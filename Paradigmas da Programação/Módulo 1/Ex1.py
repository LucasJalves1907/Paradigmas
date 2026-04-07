# ANÁLISE:
# A abordagem iterativa possui complexidade O(n), pois executa um único laço.
# Já a abordagem recursiva ingênua possui complexidade O(2^n), pois cada chamada
# gera duas novas chamadas, causando recomputações.
# Isso leva a:
# - grande número de chamadas de função
# - alto uso da pilha (stack frames)
# - desempenho muito inferior

def fib_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_recursivo(n):
    if n <= 1:  # Caso base
        return n
    return fib_recursivo(n-1) + fib_recursivo(n-2)


print(fib_iterativo(40))
print(fib_recursivo(40))