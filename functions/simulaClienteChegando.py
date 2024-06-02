from functions.mostraFila import mostraFila
from functions.chegouCliente import chegouCliente;
from classes.Cliente import Cliente;

def simulaClienteChegando(filaDeClientes, simulationTime, realTimeElapsed):
    if chegouCliente() == 0 and simulationTime < realTimeElapsed:
        # Cliente entra na fila
        novoCliente = Cliente(simulationTime);
        filaDeClientes.pushEnd(novoCliente);
        cliente = filaDeClientes.getFirstNode();
        # Mostra a situação da fila:
        mostraFila(cliente);

    return filaDeClientes;