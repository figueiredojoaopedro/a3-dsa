import time;
from functions.transacaoEscolhida import transacaoEscolhida;
from functions.chegouCliente import chegouCliente;
from Queue import Queue;
from Guiche import Guiche;

def main():
    expedientTotalTime = 6; # 6 hours
    realTimeElapsed = 120; # 2 minutes
    simulationTime = 0;
    beginningTime = 10; # opens at 10 am
    equivalentToOneHour = int(realTimeElapsed / expedientTotalTime);

    guiches = Queue();
    # criacao de 3 Guiches 
    guiches.push(Guiche());
    guiches.push(Guiche());
    guiches.push(Guiche());

    filaDeClientes = Queue();
    maiorTempoDeTransacao = 0;

    # Expediente:
    print("{}:00 Horas".format(beginningTime))
    while simulationTime < realTimeElapsed:
        # tell us the simulation time
        print("simulation time: {}".format(simulationTime));
        if((simulationTime == 20 
            or simulationTime == 40 
            or simulationTime == 60 
            or simulationTime == 80 
            or simulationTime == 100 
            or simulationTime == 120) and simulationTime % equivalentToOneHour == 0):
            beginningTime += 1; # add + 1 hour
            print("{}:00 Horas".format(beginningTime));
        
        # cliente chega:
        if(chegouCliente() == 0):
            # Cliente entra na fila
            filaDeClientes.pushEnd(simulationTime);
            cliente = filaDeClientes.getFirstNode();

            # mostra a situacao da fila:
            while cliente != None:
                print("cliente: {}".format(cliente.getData()));
                cliente = cliente.getNextNode();
            print("Comprimento da fila: {}".format(filaDeClientes.lgt));

        # checa se há guiche vazio
        print("\n");
        guiche = guiches.getFirstNode();
        while guiche != None:
            if(guiche.getData().getTempoTransacao() == 0 and filaDeClientes.lgt > 0): # se for false...
                # guiche livre
                guiche.getData().setTempoTransacao(transacaoEscolhida()); # set ocupacao true
                # remove primeira posicao fila
                print("Cliente Atendido: {}" .format(filaDeClientes.getFirstNode().getData()));
                filaDeClientes.popBegin();
            
            print("Guiche Ocupação: {}".format(guiche.getData().getTempoTransacao()));
            guiche = guiche.getNextNode();
        print("\n");

        # decresce 1 segundo do tempo de ocupacao dos guiches:
        guiche = guiches.getFirstNode();
        while guiche != None:
            if(guiche.getData().getTempoTransacao() > 0):
                guiche.getData().setTempoTransacao(guiche.getData().getTempoTransacao() - 1);
            guiche = guiche.getNextNode();
        
        time.sleep(2);
        simulationTime += 1;

    # escrever relatorio:
    # with open("Relatorio.md", "w", enconding="utf-8") as file:
    #   file.write(relatorio_content);

if __name__ == "__main__":
    main()