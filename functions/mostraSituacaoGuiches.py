def mostraSituacaoGuiches(guiches):
    guiche = guiches.getFirstNode();
    while guiche != None:
        print("Guichê Ocupação: {}".format(guiche.getData().getTempoTransacao()));
        guiche = guiche.getNextNode();