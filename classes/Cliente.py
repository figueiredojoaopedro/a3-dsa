
class Cliente:
    def __init__(self, value):
        self.tempoEsperaFila = 0;
        self.tempoEntrada = value;
    
    def getTempoEntrada(self):
        return self.tempoEntrada;

    def setTempoEntrada(self, value):
        self.tempoEntrada = value;
    
    def setTempoEsperaFila(self, tempo):
        self.tempoEsperaFila = tempo;
    
    def getTempoEsperaFila(self):
        return self.tempoEsperaFila;