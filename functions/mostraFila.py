def mostraFila(cliente):
    print("Fila:")
    print("----------------------------")
    while cliente != None:
        print("Cliente: {}".format(cliente.getData().getTempoEntrada()))
        cliente = cliente.getNextNode()
    print("----------------------------")