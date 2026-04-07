# ANÁLISE:
# Caso base: quando o elemento é encontrado
# Passo recursivo: percorrer subestruturas (dicionários)
# A recursão permite explorar estruturas hierárquicas naturalmente.

def buscar(pasta, nome):
    if nome in pasta:  # caso base
        return True

    for v in pasta.values():
        if isinstance(v, dict):  # passo recursivo
            if buscar(v, nome):
                return True

    return False


dados = {"a": {"b": {"arquivo.txt": None}}}

print(buscar(dados, "arquivo.txt"))