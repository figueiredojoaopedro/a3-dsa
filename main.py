import time;
from functions.transacaoEscolhida import transacaoEscolhida;
from functions.chegouCliente import chegouCliente;
from functions.initializingGuiches import initializingGuiches

def main():
    expedientTotalTime = 6; # 6 hours
    realTimeElapsed = 120; # 2 minutes
    simulationTime = 0;
    beginningTime = 10; # opens at 10 am
    equivalentToOneHour = int(realTimeElapsed / expedientTotalTime);

    guiche = initializingGuiches();

    print("{} Horas".format(beginningTime))
    while simulationTime < realTimeElapsed:
        # tell us the simulation time
        if(simulationTime % equivalentToOneHour == 0):
            beginningTime += 1; # add + 1 hour
            print("{} Horas".format(beginningTime));
        
        # cliente chega:
        if(chegouCliente() == 0):
            print("Cliente chegou");
            # cliente entra na fila


        # checa se há guiche vazio

        # primeiro da fila entra no guiche

        # cliente escolhe transacao

        # time.sleep(1);
        simulationTime += 1;

    print("teste {}".format(transacaoEscolhida()));

    print("teste 2 {}".format(chegouCliente()));

if __name__ == "__main__":
    main()