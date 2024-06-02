
def atualizaTempoEsperaNaFila(filaDeClientes):
    print("\n")
    if (filaDeClientes.lgt > 0):
        cliente = filaDeClientes.getFirstNode();
        while cliente != None:
            cliente.getData().setTempoEsperaFila(cliente.getData().getTempoEsperaFila() + 1)
            cliente = cliente.getNextNode()
    return filaDeClientes;