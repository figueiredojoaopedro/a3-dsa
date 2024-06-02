from functions.transacaoEscolhida import transacaoEscolhida;

def simulaEntradaGuiche(guiches, filaDeClientes, totalSaquesRealizados, totalDepositosRealizados, totalPagamentosRealizados, totalTempoEspera, totalClientesAtendidos):
    print("\n");

    # faz o loop na lista de guiches
    guiche = guiches.getFirstNode();
    while guiche != None:
        if guiche.getData().getTempoTransacao() == 0 and filaDeClientes.lgt > 0:  # se for false guiche livre
            # Atualizar contagem de operações
            tempoTransacao = 0;
            transacao = transacaoEscolhida();
            
            if transacao == 0:
                tempoTransacao = 30;
                totalSaquesRealizados += 1;

            if transacao == 1:
                tempoTransacao = 60;
                totalDepositosRealizados += 1;
            
            if transacao == 2:
                tempoTransacao = 90;
                totalPagamentosRealizados += 1;
            
            guiche.getData().setTempoTransacao(tempoTransacao);  # set ocupação true
            
            print("Cliente Atendido: {}".format(filaDeClientes.getFirstNode().getData().getTempoEntrada()));
            # adiciona ao total do tempo de espera
            totalTempoEspera += filaDeClientes.getFirstNode().getData().getTempoEsperaFila();
            filaDeClientes.popBegin(); # Remove primeira posição da fila

            totalClientesAtendidos += 1;

        guiche = guiche.getNextNode();

    return guiches, filaDeClientes, totalSaquesRealizados, totalDepositosRealizados, totalPagamentosRealizados, totalTempoEspera, totalClientesAtendidos;