from node import Node
from port import Port



class SubnetIO(Node):

    def __init__(self, ioType = "IN"):
        super(SubnetIO, self).__init__()

        self._ioType = ioType #the type of the node (Input or Output)
        self._portsPairs = []#list of port pairs that should transfer IP between each other without any changes


    def addPort(self, portType = None, dataType = None, name = None):
        #Redefined 
        # [ [portIN, portOUT], ... ]

        self._inputs.append(Port(dataType = dataType, portType = "IN", name = name + "_IN", nodePointer = self))
        portIN = self._inputs[-1]
        self._outputs.append(Port(dataType = dataType, portType = "OUT", name = name + "_OUT", nodePointer = self))
        portOUT = self._outputs[-1]

        self.addPair(portIN=portIN, portOUT=portOUT)

        return self._portsPairs[-1]  


    def addPair(self, portIN = None, portOUT = None):

        if not portIN or not portOUT:
            return

        pair = [portIN, portOUT]

        self._portsPairs.append(pair)

    def run(self):

        #set values from Input to Output ports 
        #using ports pairs

        for i in self._portsPairs:
            v = i[0].getValue()
            i[1].setValue(v)




class Subnet(object):

    def __init__(self):

        super(Subnet, self).__init__()
        self._includes = []             #list of included nodes
        self._propagatedInputs = []
        self._propagatedOutputs = []
        self._subnetIN = None             #Start node of the Subnet
        self._subnetOUT = None            #End node of the Subnet
        self.initSubnetIO()


    def initSubnetIO(self):
        """
        initialize Subnet input and Output nodes
        """
        self._subnetIN    = SubnetIO(ioType="IN")
        self._subnetOUT   = SubnetIO(ioType="OUT")


    def includeNode(self, node = None):
        """
        Adds a node to the Subnet instance
        """
        if str(type(node)) == "<type 'list'>":
            self._includes = node
        else:
            #check if node is Node class or Loop class
            self._includes.append(node)


    def getIncludes(self):
        return self._includes


    def propPort(self, port = None):
        """
        Propagates the given port.
        Depends on - if it's IN or OUT port - it creates port in subnetIN or subnetOUT and connects port with subnetPort
        if the given port is initially connected to some other port - it breaks that connection and reconnects as seen below:
            currentPort -> subnetPort -> outsidePort
        """


        if not port:
            return 

        connectedNode = port.getConnectedNode() #get connected node | or None
        connectedPort = port.getConnectedPort() #get connected port | or None
        masterNode = port.getMasterNode()       #get port's Node

        propType = None

        #Analyze
        if not connectedNode:
            
            # print "Propagate {}coming port {} for node {}".format(port.getType(), port.getName(), masterNode.getName())

            propType = "prop"

        else:
            if connectedNode in self.getIncludes():
                #don't propagate (don't do anything)
                pass
                # print "Don't propagate {}coming port  {} for node {}".format(port.getType(), port.getName(), masterNode.getName())
           
            else:
                #propagate
                # print "Propagate {}coming port {} for node {}".format(port.getType(), port.getName(), masterNode.getName())

                propType = "propConnect"


        #Propagate
        if propType == "propConnect":

            #add port to subnetIN our subnetOUT node
            ioPort = None
            if port.getType() == "IN":
                ioPort = self._subnetIN.addPort(dataType = port.getDataType(), name = port.getMasterNode().getName() + "_" + port.getName())
                self._propagatedInputs.append(ioPort)
            elif port.getType() == "OUT":
                ioPort = self._subnetOUT.addPort(dataType = port.getDataType(), name = port.getMasterNode().getName() + "_" + port.getName())
                self._propagatedOutputs.append(ioPort)

            #detach port from outsidePort
            port.detachConnection()

            #connect compIN/OUT -> port
            if port.getType() == "IN":
                port.connect(source = ioPort[1])
                ioPort[0].connect(source = connectedPort)


            elif port.getType() == "OUT":
                port.connect(target = ioPort[0])
                ioPort[1].connect(target = connectedPort)

        elif propType == "prop":
            #just connect port -> In/Ou comp port
            pass




    def build(self):
        """
        For all included nodes finds all fist-incoming node ports and last-outgoing ports
        Connects those ports to related ports of included nodes
        Unconnects included nodes from the root
        """

        for i in self._includes:
            
            # get input ports
            in_ports = i.getInputPorts()
            for iP in in_ports:
                self.propPort(port = iP)

            # get out ports
            out_ports = i.getOutputPorts()
            for oP in out_ports:
                self.propPort(port = oP)


    def getLoopRelatives(self):
        """
        if we have loop_        stat or loop_end included
            then if it won't find loop_relative node in includes - don't generate ports
        """
        pass

    # def run(self):
    #     """
    #     Must run internal structure - like in manager
    #     Current node in Subnet is the Subnet Itself - and run comes from Outcoming Subnet ports
    #     """

        # for i in self.getOutputPorts():
        #     print i, i.getName(), i.getType()
            
        #     DFM = DataFlowManager()
        #     calculatedValue = DFM.calculatePort(port = i)
            # i.setValue(calculatedValue)

        



