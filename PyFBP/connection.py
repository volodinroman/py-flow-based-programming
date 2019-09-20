class Connection(object):

    def __init__(self, source = None, target = None):

        self._sourcePort = source # port where connection starts
        self._targetPort = target #port where connection ends

    def setSourcePort(self, source = None):
        self._sourcePort = source

    def setTargetPort(self, target = None):
        self._targetPort = target

    def getSourcePort(self):
        return self._sourcePort

    def getTargetPort(self):
        return self._targetPort

    def clear(self):
        self._sourcePort = None
        self._targetPort = None
