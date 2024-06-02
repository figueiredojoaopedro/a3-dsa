
def decresceTempoDeOcupacao(guiches, tempoTotalTodosCaixas):
    guiche = guiches.getFirstNode();
    aux = 0;
    while guiche != None:
        aux += guiche.getData().getTempoTransacao();
        if guiche.getData().getTempoTransacao() > 0:
            guiche.getData().setTempoTransacao(guiche.getData().getTempoTransacao() - 1);

        guiche = guiche.getNextNode();
    tempoTotalTodosCaixas = aux;

    return guiches, tempoTotalTodosCaixas;
