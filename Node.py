class Node:
    def __init__(self, value):
        self.data = value;
        self.tempoEsperaFila = 0;
        self.prevNode = self.nextNode = None;

    def getData(self):
        return self.data;

    def setData(self, data):
        self.data = data;
    
    def setTempoEsperaFila(self, tempo):
        self.tempoEsperaFila = tempo;
    
    def getTempoEsperaFila(self):
        return self.tempoEsperaFila;

    def display(self):
        print("Data: " + self.data);

    def getNextNode(self):
        return self.nextNode;

    def getPrevNode(self): 
        return self.prevNode;

    def setNextNode(self, nextNode):
        self.nextNode = nextNode;

    def setPrevNode(self, prevNode):
        self.prevNode = prevNode;
