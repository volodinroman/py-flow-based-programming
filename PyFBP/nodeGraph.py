from port import Port
from connection import Connection
from node import Node
from loop import NodeLoop, Loop 

class NodeGraph(object):
    """
    NodeGraph controlls the way how connected nodes interract with each other
    """

    def __init__(self):
        """[Constructor]"""
        self.nodesList          = []     # list of nodes in our NodeGraph
        self.connectorsList     = []     # list of all connection lines in our NodeGraph
        self.currentNode        = None   

    def setCurrentNode(self, node = None):
        self.currentNode = node

    def addNode(self, node = "Test", nodeName = None):
        #search for nodeName module
        # if exist - import data
        # exec(NodeType()) 


        _node = Node(nodeName = nodeName)
        self.nodesList.append(_node)
        return _node

    # def connectNodes(self, sourcePort = None, targetPort = None):

    #     con = Connection(source = sourcePort, target = targetPort)
    #     sourcePort.setConnetionLine(line = con)
    #     targetPort.setConnetionLine(line = con)

    #     return con


    #---------------------- processing

    # def defence(self, node = None):

    #     if not Node:
    #         return

    #     for i in node.getInputPorts():
    #         if not i.getValue():
    #             print "{} has no value".format(i.getName())



    def calculatePort(self, port = None):

        # check pas
        if not port:
            return None

        _out = port.getValue() # get passed-in port value
        if _out != None: # if it has any value assigned (not None)
            return _out

        """#! REMOVE #get outPort -> port line | 
        # line = port.getConnectionLine() # return L1
        # #get line source 
        # sourcePort = line.getSourcePort()"""

        # get the incoming connection source port (output of another node)
        sourcePort = port.getConnectedPort() 
        if not sourcePort:
            return 0 #TODO return and do something with None result

        #check if the source port already has some value assigned
        sourcePort_value = sourcePort.getValue()
        if sourcePort_value: 
            _out = sourcePort_value
            return _out  # idea is: connected source port already has a calculated _out, but _out hasn't been sent to the target yet
        
        else:
            #calculate source node (get all input ports and calculate all outputs)
            sourcePortNode = sourcePort.getMasterNode() 
            inputs = sourcePortNode.getInputPorts() #get all inputs
            for i in inputs:
                 if not i.getValue(): #if any input has no value
                    incoming_value = self.calculatePort(i) #get value from incoming node connected to this input
                    if incoming_value:
                        i.setValue(incoming_value)

            #Run source node (calculate outputs)
            sourcePortNode.run()

            for output in sourcePortNode.getOutputPorts():
                # get the required output port from the source node
                if sourcePort == output:
                    _out = output.getValue()

            #get the node of the current port
            masterNode = port.getMasterNode()

            #if LOOP
            if masterNode.getNodeType() == "Loop":
                
                loopData = masterNode.getLoopData() 

                if masterNode.isNodeEnd(): #only if it's loop end node
                    
                    if loopData.isDone(): #increment +=1 | compare
                        print ("Loop is done")
                        loopData.zeroOutLoop()
                    else:
                        #_out  = is our current loop output
                        #but iteration has not been done yet
                        #cleanup loop start
                        loopStart = loopData.getStart()
                        self.cleanupUpstream(node = loopStart,  cleanLoop = False) 
                        #set loopStart input value = _out
                        loopData.getStartInput().setValue(_out)
                        _out = self.calculatePort(port = loopData.getEndInput()) #run nodes again until it gets to the end_loop
                        loopData.getEndOutput().setValue(_out)
            
        return _out


    def start(self, node = None):
        """
        @param  node  [class instance]  the node which results we want to get 
        """

        #if no node has been specified - cancel
        if not node:
            return 0

        #Make sure all required input ports have values assigned 
        #It won't be possible to calculate this node if it's not provided with some values
        for i in node.getInputPorts():

            #In case current input port does not have any value assigned
            #   Retrieve value from incoming connection (if possible)
            if not i.getValue(): 
                i.setValue(self.calculatePort(port = i))

        #run node with calculated input values
        node.run()


    def cleanupUpstream(self, node = Node, cleanLoop = True):

        print ("cleaning node {}".format(node.getName()))

        #if we meet loop End first time - clean up steam, starting from loop Start
        if node.getNodeType() == "Loop" and node.isNodeEnd() and cleanLoop:
            print ("Here we get ", node.getName())
            loopStart = node.getLoopData().getStart()
            self.cleanupUpstream(node = loopStart, cleanLoop = False)
            
        else:
            #if it's a default node or Loop Start
            node.cleanUpPorts() #clean all node ports' values

            #if node has any output connections - cleanup connected nodes 
            for i in node.getOutputPorts(): 
                line = i.getConnectionLine()
                if line:
                    upstreamNode = line.getTargetPort().getMasterNode() #get the next upstream node
                    self.cleanupUpstream(upstreamNode, cleanLoop = cleanLoop) #run cleanUp for this node

    
    """
    Utilities
    """

    def getNodeList(self):
        return self.nodesList

    def getCurrentNode(self):
        return self.currentNode
