import random;
from Queue import Queue;
from functions.transacaoEscolhida import transacaoEscolhida;
from functions.chegouCliente import chegouCliente;

def main():
    transacaoCliente = transacaoEscolhida();
    print("teste {}".format(transacaoCliente));

    print("teste 2 {}".format(chegouCliente()));

if __name__ == "__main__":
    main()