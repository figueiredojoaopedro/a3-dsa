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
    clock = 0;

    guiches = Queue(None, None);
    # criacao de 3 Guiches 
    guiches.push(Guiche());
    guiches.push(Guiche());
    guiches.push(Guiche());

    filaDeClientes = Queue(None, None);

    # Expediente:
    print("{}:00 Horas".format(beginningTime))
    while simulationTime < realTimeElapsed:
        time.sleep(3);
        # tell us the simulation time
        if((equivalentToOneHour == 20 
            or equivalentToOneHour == 40 
            or equivalentToOneHour == 60 
            or equivalentToOneHour == 80 
            or equivalentToOneHour == 100 
            or equivalentToOneHour == 120) and simulationTime % equivalentToOneHour == 0):
            beginningTime += 1; # add + 1 hour
            print("{}:00 Horas".format(beginningTime));
        
        # cliente chega:
        if(chegouCliente() == 0):
            # Cliente entra na fila
            filaDeClientes.pushEnd(simulationTime);
            print("Cliente chegou {}".format(filaDeClientes.length()));
        
        # mostra como esta a situacao da fila
        if(filaDeClientes.length() > 0):
            clientePos = filaDeClientes.getFirstNode();
            pos = 0;
            while clientePos != None:
                pos += 1;
                print("{} => {}".format(pos, clientePos.getData()));
                clientePos = clientePos.getNextNode();

        # checa se há guiche vazio
        guiche = guiches.getFirstNode();
        while guiche != None:
            print("Guiche tempo: {}".format(guiche.getData().getTempoTransacao()));
            if(guiche.getData().getTempoTransacao() == 0): # se for false...
                # guiche livre
                guiche.getData().setTempoTransacao(transacaoEscolhida()); # set ocupacao true
                # remove primeira posicao fila
                print("Cliente atendido: {}" .format(filaDeClientes.getFirstNode()));
                filaDeClientes.popBegin();

            guiche = guiche.getNextNode();
        
        # decresce 1 segundo do tempo de ocupacao dos guiches:
        guiche = guiches.getFirstNode();
        while guiche != None:
            guiche.getData().setTempoTransacao(guiche.getData().getTempoTransacao() - 1);
            print("Tempo de transacao {}".format(guiche.getData().getTempoTransacao()));
            guiche = guiche.getNextNode();
        
        simulationTime += 1;

if __name__ == "__main__":
    main()