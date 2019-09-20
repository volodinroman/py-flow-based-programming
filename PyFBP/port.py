from connection import Connection

class Port(object):

    def __init__(self, dataType = "float", portType = "IN", name = "Test", nodePointer = None):
        
        self.dataType = dataType           #ports that are connected must keep data of the same type
        self.portType = portType           #there are two types - IN / OUT
        self.value = None                  #the actual port value
        self.name = name                   #the visual name of the port
        self.node = nodePointer            #pointer to the master node that contains this port
        self.line = None                   #connection line  that connects this port to another one
        self.id = str(hex(id(self)))[2:]   #self id

    def getDataType(self):
        return self.dataType

    def setDataType(self, dataType = None):
        if not dataType:
            return 

        self.dataType = dataType

    def getName(self):
        return self.name

    def setName(self, name = None):
        self.name = name

    def getType(self):
        return self.portType

    def setValue(self, value = None):
        self.value = value

    def getValue(self):
        return self.value

    def delValue(self):
        self.value = None

    def setConnetionLine(self, line = None):
        self.line = line

    def getConnectionLine(self):
        return self.line

    

    def getConnectedPort(self):

        # only if the port is connected to some other port
        if self.getConnectionLine():

            if self.portType == "IN":
                return self.line.getSourcePort()
            if self.portType == "OUT":
                return self.line.getTargetPort()

    def getConnectedNode(self):

        if self.getConnectionLine() and self.getConnectedPort():

            return self.getConnectedPort().getMasterNode()

        return None 


    def connect(self, port = None, source = None, target = None):

        """
        Connects current port to another port 
        Only two types of connections are available: target->source, source->target
        if current port type is "IN" -> connect to "OUT" (source)
            or if "OUT" -> connect to "IN" (target)
        """
        if not source and not target:

            source = None 
            target = None
            #current port is "IN" - it connects only to Source ("OUT")
            if self.portType == "IN":
                source = port 
                target = self
            elif self.portType == "OUT":
                source = self
                target = port

        else:
            if source and not target:
                target = self
            elif target and not source:
                source = self

        con = Connection(source = source, target = target)
        source.setConnetionLine(line=con)
        target.setConnetionLine(line=con)

    def _delConnectionLine(self):
        self.line = None
        
    def removeConnection(self):
        """
        Break connection of the current node with source/target port 
        Delete line instance from everywhere
        """
        
        self.getConnectedPort()._delConnectionLine() #from connected port - del Line info

        self.getConnectionLine().clear() #from connected line - del all ports info

        self._delConnectionLine() # del line info from the current port



    def getMasterNode(self):
        return self.node

    def getPortType(self):
        return self.portType
