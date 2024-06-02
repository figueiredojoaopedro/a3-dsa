from functions.defineTempoReal import defineTempoReal;
from functions.simulaClienteChegando import simulaClienteChegando;
from functions.mostraSituacaoGuiches import mostraSituacaoGuiches;
from functions.simulaEntradaGuiche import simulaEntradaGuiche;
from functions.atualizaTempoEsperaNaFila import atualizaTempoEsperaNaFila;
from functions.decresceTempoDeOcupacao import decresceTempoDeOcupacao;
from functions.criaStringRelatorio import criaStringRelatorio;
from functions.gravarRelatorio import gravarRelatorio;
from TAD.Queue import Queue
from classes.Guiche import Guiche


def main():
    realTimeElapsed = 21600; # 6 hours in seconds 21600
    simulationTime = 1;

    guiches = Queue();
    # criação de 3 Guiches
    guiches.push(Guiche());
    guiches.push(Guiche());
    guiches.push(Guiche());

    # cria a fila de clientes
    filaDeClientes = Queue();

    totalClientesAtendidos = 0; # 

    totalSaquesRealizados = 0; # 
    totalDepositosRealizados = 0; # 
    totalPagamentosRealizados = 0; # 
    

    totalTempoEspera = 0; # Para calcular o tempo médio de espera

    tempoTotalTodosCaixas = 0; # para saber quanto tempo falta nas operacoes

    # Expediente:
    while simulationTime <= realTimeElapsed or filaDeClientes.lgt > 0 or tempoTotalTodosCaixas > 0:
        # Diz o tempo de simulação
        print("Tempo de simulação: {}".format(simulationTime));

        # Cliente chega:
        filaDeClientes = simulaClienteChegando(filaDeClientes, simulationTime, realTimeElapsed);
        print("Comprimento da fila: {}".format(filaDeClientes.lgt));

        # printa a situacao dos guiches
        mostraSituacaoGuiches(guiches);

        # Verifica se há guichê vazio
        (guiches, 
        filaDeClientes, 
        totalSaquesRealizados, 
        totalDepositosRealizados, 
        totalPagamentosRealizados, 
        totalTempoEspera, 
        totalClientesAtendidos) = simulaEntradaGuiche(
            guiches, 
            filaDeClientes, 
            totalSaquesRealizados, 
            totalDepositosRealizados, 
            totalPagamentosRealizados, 
            totalTempoEspera, 
            totalClientesAtendidos
        )
 
        # atualiza o tempo de espera de todo mundo na fila
        filaDeClientes = atualizaTempoEsperaNaFila(filaDeClientes);

        # Decresce 1 segundo do tempo de ocupação dos guichês:
        guiches, tempoTotalTodosCaixas = decresceTempoDeOcupacao(guiches, tempoTotalTodosCaixas);

        simulationTime += 1

    totalTempoEsperaMins = totalTempoEspera / 60;
    print("Total tempo da fila {:.2f} mins".format(totalTempoEsperaMins));

    # Calcula o tempo extra de simulação até que todos os guichês estejam desocupados
    tempoExtra = (simulationTime - realTimeElapsed) / 60;
    print("Tempo do trabalho extra: {:.2f} minuto(s)".format(tempoExtra));

    # Calcula o tempo médio de espera de cada cliente
    mediaEspera = totalClientesAtendidos / totalTempoEsperaMins;

    # Escrever relatório:
    relatorio = criaStringRelatorio(totalClientesAtendidos, totalSaquesRealizados, totalDepositosRealizados, totalPagamentosRealizados, tempoExtra, mediaEspera);

    # Escreve o arquivo no mesmo diretorio
    gravarRelatorio(relatorio);


if __name__ == "__main__":
    main()

