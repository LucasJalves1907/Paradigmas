# ANÁLISE:
# Lazy evaluation gera dados sob demanda.
# Evita carregar grandes volumes na memória.
# Ideal para dados infinitos ou streams.

def logs():
    i = 0
    while True:
        yield i
        i += 1


g = logs()

for _ in range(5):
    print(next(g))