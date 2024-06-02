from TAD.Node import Node;

class Queue:
    def __init__(self):
        self.firstNode = None;
        self.lastNode = None;
        self.lgt = 0;

    def isEmpty(self): 
        return (self.firstNode == None);

    def leng(self):
        return self.lgt;

    def getFirstNode(self):
        return self.firstNode;

    def getLastNode(self):
        return self.lastNode;

    def push(self, value): # insert node in the beginning of the queue
        newNode = Node(value);
        self.lgt += 1;

        if(self.isEmpty()):
            self.firstNode = self.lastNode = newNode;
            return;
        
        self.firstNode.prevNode = newNode;
        newNode.setNextNode(self.firstNode);
        self.firstNode = newNode;

    def pushEnd(self, value):
        newNode = Node(value);
        self.lgt += 1;

        if(self.isEmpty()):
            self.firstNode = self.lastNode = newNode;
            return;

        self.lastNode.nextNode = newNode; # the last node earns a new guy in front of it
        newNode.prevNode = self.lastNode; # the new last node earns its pointer to the node behind
        self.lastNode = newNode; # the new node in the end becomes the lastnode itself


    def insertNode(self, key, value): # insert node in a specific position from the queue
        currentNode = self.firstNode;

        if(currentNode == None):
            return False;

        while(currentNode.getData() != key):
            currentNode = currentNode.nextNode;
            if(currentNode == None):
                return False; # Cannot find it

        self.lgt += 1;
        # creating a new node
        newNode = Node(value);

        if(currentNode == self.lastNode):
            self.lastNode.nextNode = newNode; # the last node earns a new guy in front of it
            newNode.prevNode = self.lastNode; # the new last node earns its pointer to the node behind
            self.lastNode = newNode; # the new node in the end becomes the lastnode itself
        else:
            newNode.setNextNode(currentNode.getNextNode);
            currentNode.getNextNode().setPrevNode(newNode);
            newNode.setPrevNode(currentNode);
            currentNode.setNextNode(newNode);

        return True;

    def popBegin(self):
        temp = self.firstNode;
        self.lgt -= 1;

        # if there is only one node or there is anything in the list, the result would be an empty list anyway.
        if((self.isEmpty()) or (self.firstNode.getNextNode() == None)):
            self.lastNode = self.firstNode = None;
            return temp;

        self.firstNode.getNextNode().setPrevNode(None);
        self.firstNode = self.firstNode.getNextNode();

        return temp;

    def popEnd(self):
        temp = self.lastNode;
        self.lgt -= 1;

        # if there is only one node or there is anything in the list, the result will be an empty list.
        if(self.isEmpty() or self.lastNode.getPrevNode() == None):
            self.lastNode = self.firstNode = None;
            return temp;

        # we get the last but one and point the nextNode pointer to None and set itself as the lastNode of the queue
        self.lastNode.getPrevNode().setNextNode(None);
        self.lastNode = self.lastNode.getPrevNode();

        return temp;

    def pop(self, key):
        currentNode = self.firstNode;

        # if the list is empty, we return none
        if(self.isEmpty()):
            return None;

        # traversing linearly through the list while the data isn't equal to the key
        while(currentNode.getData() != key):
            currentNode = currentNode.getNextNode();
            if(currentNode == None):
                return None;

        self.lgt -= 1;
        # if it's the first node, we do just as if it was popBegin
        if(currentNode == self.firstNode):
            self.firstNode = self.firstNode.getNextNode();
            self.firstNode.setPrevNode(None);
            return currentNode;

        # if it's the last node, we do just as if it was popEnd
        if(currentNode == self.lastNode):
            self.lastNode = self.lastNode.getPrevNode();
            self.lastNode.setNextNode(None);
            return currentNode;

        # if it's in the middle, we point the previous node to the next node and the opposite
        currentNode.getPrevNode().setNextNode(currentNode.getNextNode());
        currentNode.getNextNode().setPrevNode(currentNode.getPrevNode());
        return currentNode();

        
        