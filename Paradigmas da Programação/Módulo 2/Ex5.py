# ANÁLISE:
# Python utiliza call-by-sharing:
# - a função recebe a referência do objeto
# - listas são mutáveis
# Portanto, alterações dentro da função afetam o objeto original,
# causando mudanças irreversíveis no estado do programa.

def aplicar_desconto(lista):
    for i in range(len(lista)):
        lista[i] -= 10


estoque = [100, 200, 300]

aplicar_desconto(estoque)

print(estoque)