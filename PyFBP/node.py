from port import Port



class Node(object):

    """
    A Node is a calculative unit with some properties and ports.
    In order to run the node - we should feed in some values into Input Ports
    As soon as all input ports have some values (data) - "run" method calculates and feeds in output ports
    If one of the input ports has None value - it checks the connected port if it has any value in it
        if no - it goes deeper to other nodes to get some value
            if no value received - it sets Valid = False and sends signal to other downstream nodes that calculation can't be completed

    """

    def __init__(self, nodeName = 'Default', nodeType = "Default"):

        self.name = nodeName               #visual node name
        self.id = str(hex(id(self)))[2:]   #self id
        self.inputs = []                   #collects all input ports
        self.outputs = []                  #collects all output ports
        self.valid = True                  #we can stop calculating downstream if it's not valid
        self.nodeType = nodeType           #Default | Loop | Subnet


    def getName(self):
        return self.name

    def setName(self, name = None):
        if not name:
            return
        self.name = name

    def getNodeType(self):
        return self.nodeType

    def setNodeType(self, nodeType = None):
        if not nodeType:
            return
        self.nodeType = typ

    def getId(self):
        return self.id

    def makeInvalid(self):
        self.valid = False

    def getInputPorts(self):
        return self.inputs

    def getOutputPorts(self):
        return self.outputs

    def addPort(self, portType = None, dataType = None, name = None):

        if portType == "IN": #add to input list
            self.inputs.append(Port(dataType = dataType, portType = portType, name = name, nodePointer = self))
            return self.inputs[-1]

        elif portType == "OUT": #add to output list
            self.outputs.append(Port(dataType = dataType, portType = portType, name = name, nodePointer = self))
            return self.outputs[-1]

    def addInput(self, dataType, name = None):

        self.inputs.append(Port(dataType = dataType, portType = "IN", name = name, nodePointer = self))
        return self.inputs[-1]

    def addOutput(self, dataType, name = None):

        self.outputs.append(Port(dataType = dataType, portType = "OUT", name = name, nodePointer = self))
        return self.outputs[-1]

    def cleanUpPorts(self):

        for i in self.getInputPorts():
            i.delValue()

        for i in self.getOutputPorts():
            i.delValue()

    def run(self):
        """
        Virtual method
        Run() should feed output ports with some results
        Or it should be marked Bad and return False to outcoming nodes
        """
        
        #calculate node
        print ("{} run()".format(self.getName()))

        #feed outputs
        result = 0
        for i in self.getInputPorts():
            v = i.getValue()
            # print v, self.getName()
            if v:
                result += float(v)

        for i in self.getOutputPorts(): #for every output port
            i.setValue(result) #set test value
            print ("Output: {}".format(i.getValue()))

        # print ""



    
