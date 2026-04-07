# ANÁLISE:
# Em sistemas grandes, o modelo procedural sofre com:
# - alto acoplamento
# - múltiplas funções alterando o mesmo estado
# - risco de inconsistência
# Isso torna o sistema difícil de manter e escalar.
# Esse problema motiva o uso de POO, com encapsulamento de dados.

class Sistema:
    def __init__(self):
        self.pacientes = []
        self.leitos = 10
        self.caixa = 0


def internar(s, nome):
    if s.leitos > 0:
        s.pacientes.append(nome)
        s.leitos -= 1
        s.caixa += 500


s = Sistema()

internar(s, "João")

print(s.pacientes, s.leitos, s.caixa)