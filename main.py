import time
from functions.transacaoEscolhida import transacaoEscolhida
from functions.chegouCliente import chegouCliente
from Queue import Queue
from Guiche import Guiche


def main():
    expedientTotalTime = 6  # 6 hours
    realTimeElapsed = 7 # 2 minutes
    simulationTime = 1
    beginningTime = 10  # opens at 10 am
    equivalentToOneHour = int(realTimeElapsed / expedientTotalTime)

    guiches = Queue()
    # criação de 3 Guiches
    guiches.push(Guiche())
    guiches.push(Guiche())
    guiches.push(Guiche())

    # cria a fila de clientes
    filaDeClientes = Queue()

    totalClientesAtendidos = 0 # 

    totalSaquesRealizados = 0 # 
    totalDepositosRealizados = 0 # 
    totalPagamentosRealizados = 0 # 
    totalOperacoesRealizadas = 0

    totalTempoEspera = 0  # Para calcular o tempo médio de espera

    tempoTotalTodosCaixas = 0

    # Expediente:
    print("{}:00 Horas".format(beginningTime))
    while simulationTime <= realTimeElapsed or filaDeClientes.lgt > 0 or tempoTotalTodosCaixas > 0:
        # Diz o tempo de simulação
        print("Tempo de simulação: {}".format(simulationTime))
        if ((simulationTime == 20
             or simulationTime == 40
             or simulationTime == 60
             or simulationTime == 80
             or simulationTime == 100
             or simulationTime == 120) and simulationTime % equivalentToOneHour == 0):
            beginningTime += 1  # add + 1 hour
            print("{}:00 Horas".format(beginningTime))

        # Cliente chega:
        if chegouCliente() == 0 and simulationTime < realTimeElapsed:
            # Cliente entra na fila
            filaDeClientes.pushEnd(simulationTime)
            cliente = filaDeClientes.getFirstNode()
            
            # Mostra a situação da fila:
            print("Fila:")
            print("----------------------------")
            while cliente != None:
                print("Cliente: {}".format(cliente.getData()))
                cliente = cliente.getNextNode()
            print("----------------------------")
        print("Comprimento da fila: {}".format(filaDeClientes.lgt))


        # printa a situacao dos guiches
        guiche = guiches.getFirstNode()
        while guiche != None:
            print("Guichê Ocupação: {}".format(guiche.getData().getTempoTransacao()))
            guiche = guiche.getNextNode()

        # Verifica se há guichê vazio
        print("\n")
        guiche = guiches.getFirstNode()
        while guiche != None:
            if guiche.getData().getTempoTransacao() == 0 and filaDeClientes.lgt > 0:  # se for false guiche livre
                # Atualizar contagem de operações
                tempoTransacao = 0
                transacao = transacaoEscolhida()

                if transacao == 0:
                    tempoTransacao = 3
                    totalSaquesRealizados += 1

                if transacao == 1:
                    tempoTransacao = 6 
                    totalDepositosRealizados += 1
                
                if transacao == 2:
                    tempoTransacao = 9
                    totalPagamentosRealizados += 1
                
                guiche.getData().setTempoTransacao(tempoTransacao)  # set ocupação true
                totalOperacoesRealizadas += 1
                
                # Remove primeira posição da fila
                print("Cliente Atendido: {}".format(filaDeClientes.getFirstNode().getData()))
                totalTempoEspera += filaDeClientes.getFirstNode().getTempoEsperaFila()
                filaDeClientes.popBegin()

                totalClientesAtendidos += 1

            guiche = guiche.getNextNode()


        print("\n")
        if (filaDeClientes.lgt > 0):
            cliente = filaDeClientes.getFirstNode();
            while cliente != None:
                cliente.setTempoEsperaFila(cliente.getTempoEsperaFila() + 1)
                cliente = cliente.getNextNode()

        # Decresce 1 segundo do tempo de ocupação dos guichês:
        guiche = guiches.getFirstNode()
        aux = 0
        while guiche != None:
            aux += guiche.getData().getTempoTransacao()
            if guiche.getData().getTempoTransacao() > 0:
                guiche.getData().setTempoTransacao(guiche.getData().getTempoTransacao() - 1)

            guiche = guiche.getNextNode()
        tempoTotalTodosCaixas = aux

        time.sleep(2)
        simulationTime += 1

    print("Teste total tempo da fila {}".format(totalTempoEspera));


    # # Calcula o tempo extra de simulação até que todos os guichês estejam desocupados
    # tempoExtra = simulationTime - realTimeElapsed

    # # Calcula o tempo médio de espera na fila
    # tempoMedioEspera = totalTempoEspera / totalClientesAtendidos if totalClientesAtendidos > 0 else 0

    # # Escrever relatório:
    # relatorio = f"Total de Clientes Atendidos: {totalClientesAtendidos}\n"
    # relatorio += f"Total de Operações Realizadas: {totalOperacoesRealizadas}\n"
    # relatorio += f"Total de Saques Realizadas: {totalSaquesRealizados}\n"
    # relatorio += f"Total de Depositos Realizadas: {totalDepositosRealizados}\n"
    # relatorio += f"Total de Pagamentos Realizadas: {totalPagamentosRealizados}\n"
    # relatorio += f"Tempo Extra de Simulação: {tempoExtra:.2f} minutos\n"
    # relatorio += f"Tempo Médio de Espera na Fila: {tempoMedioEspera:.2f} minutos\n"


    # with open("Relatorio.md", "w", encoding="utf-8") as file:
    #     file.write(relatorio)

if __name__ == "__main__":
    main()

