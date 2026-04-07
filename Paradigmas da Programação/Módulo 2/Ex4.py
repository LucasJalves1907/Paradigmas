# ANÁLISE:
# Funções puras não alteram o estado externo, apenas retornam valores.
# Procedimentos com referência alteram diretamente variáveis externas,
# gerando efeitos colaterais, o que pode causar comportamentos inesperados.

def calcular_altitude(atual, delta):
    return atual + delta


def forcar_altitude(ref, delta):
    ref[0] += delta


alt = 1000

print(calcular_altitude(alt, 500))
print(alt)  # não muda

ref = [alt]
forcar_altitude(ref, 500)
alt = ref[0]

print(alt)