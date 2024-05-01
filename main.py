import random

class Guiche:
    def _init_(self):
        self.ocupado = False
        self.tempo_ocupado = 0

class Cliente:
    def _init_(self, horario_chegada):
        self.horario_chegada = horario_chegada
        self.tempo_espera = 0

def realizar_transacao():
    transacao = random.randint(0, 2)
    if transacao == 0:
        return "Saque", 60
    elif transacao == 1:
        return "Depósito", 90
    else:
        return "Pagamento", 120

def main():
    expediente_segundos = 21600
    fila = []
    guiches = [Guiche() for _ in range(3)]
    total_clientes_atendidos = 0
    clientes_saque = 0
    clientes_deposito = 0
    clientes_pagamento = 0
    tempo_espera_total = 0
    cronometro = 0

    while cronometro < expediente_segundos or fila:
        if random.randint(0, 29) == 0:
            fila.append(Cliente(cronometro))

        for guiche in guiches:
            if not guiche.ocupado and fila:
                cliente = fila.pop(0)
                guiche.ocupado = True
                guiche.tempo_ocupado = realizar_transacao()[1]
                cliente.tempo_espera = cronometro - cliente.horario_chegada

                if guiche.tempo_ocupado == 60:
                    clientes_saque += 1
                elif guiche.tempo_ocupado == 90:
                    clientes_deposito += 1
                elif guiche.tempo_ocupado == 120:
                    clientes_pagamento += 1

                total_clientes_atendidos += 1
                tempo_espera_total += cliente.tempo_espera

            if guiche.ocupado:
                guiche.tempo_ocupado -= 1
                if guiche.tempo_ocupado == 0:
                    guiche.ocupado = False

        cronometro += 1

    print("Número total de clientes atendidos:", total_clientes_atendidos)
    print("Número de clientes que fizeram saque:", clientes_saque)
    print("Número de clientes que fizeram depósito:", clientes_deposito)
    print("Número de clientes que fizeram pagamento:", clientes_pagamento)
    print("Tempo médio de espera na fila:", tempo_espera_total / total_clientes_atendidos)
    print("Tempo extra de expediente:", cronometro - expediente_segundos)

if _name_ == "_main_":
    main()