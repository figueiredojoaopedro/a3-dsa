import random;

def transacaoEscolhida():
    # numero de 0 a 2
    transacao = random.randint(0, 2);
    return transacao
    if(transacao == 0):
        return 3;
    if(transacao == 1):
        return 6;
    if(transacao == 2):
        return 9;