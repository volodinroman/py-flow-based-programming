from node import Node

class NodeLoop(Node):

    def __init__(self, nodeName = None, nodeType = "Loop", loopEnd = False, loop = None):

        super(NodeLoop, self).__init__()
        self._nodeType = nodeType
        self._loopEnd = loopEnd
        self._loop = loop
        self._name = nodeName

    def isNodeEnd(self):

        return self._loopEnd

    def getLoopData(self):

        return self._loop

    def run(self):
        
        #feed outputs
        if self.isNodeEnd():
            print  ("loopEnd Run()")
        else:
            print ("<<<<<< loopStart Run()")

        result = 0
        for i in self.getInputPorts():
            result = i.getValue()
        for i in self.getOutputPorts(): 
            i.setValue(result) 
            
            if self.isNodeEnd():
                print ("Output: {}  >>>>>>".format(i.getValue()))
            else:
                print ("Output: {} ".format(i.getValue()))

        print ("")
            
            
class Loop(object):

    def __init__(self, count = 1):
        self._count = count 
        self._currentLoopNumber = 0

        self._start = NodeLoop(nodeName = "Loop Start", nodeType = "Loop", loopEnd = False, loop = self)
        self._start_portInput = self._start.addPort(portType = "IN", dataType = "float", name = "In_01")
        self._start_portOutput = self._start.addPort(portType = "OUT", dataType = "float", name = "Out_01")

        self._end  = NodeLoop(nodeName = "Loop End", nodeType = "Loop", loopEnd = True, loop = self)
        self._end_portInput = self._end.addPort(portType = "IN", dataType = "float", name = "In_01")
        self._end_portOutput = self._end.addPort(portType = "OUT", dataType = "float", name = "Out_01")

    def getStart(self):
        return self._start

    def getStartInput(self):
        return self._start_portInput

    def getStartOutput(self):
        return self._start_portOutput

    def getEndInput(self):
        return self._end_portInput

    def getEndOutput(self):
        return self._end_portOutput

    def getEnd(self):
        return self._end

    def incrementLoop(self):
        self._currentLoopNumber += 1
        return self._currentLoopNumber

    def zeroOutLoop(self):
        self._currentLoopNumber = 0
        self._start_portInput.setValue(None)
        self._start_portOutput.setValue(None)
        # self._end_portInput.setValue(None)
        # self._end_portOutput.setValue(None)

    def isDone(self):

        self.incrementLoop()

        if self._currentLoopNumber == self._count:
            self.zeroOutLoop()
            return True
        else:
            return False


