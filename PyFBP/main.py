from port import Port
from connection import Connection
from node import Node
from loop import NodeLoop, Loop 
from nodeGraph import NodeGraph
from subnet import Subnet

def main():

    # import sys
    # for i in sys.path:
    #     print(i)

  
    # the one that rules them all
    nodeGraph = NodeGraph()

    node_A = nodeGraph.addNode(nodeName = "node_A")
    node_A_input01 = node_A.addPort(portType = "IN", dataType = "float", name = "input01").setValue(3)
    node_A_output01 = node_A.addPort(portType = "OUT", dataType = "float", name = "output01")

    node_B = nodeGraph.addNode(nodeName = "node_B")
    node_B_input01 = node_B.addPort(portType = "IN", dataType = "float", name = "input01").setValue(7)
    node_B_output01 = node_B.addPort(portType = "OUT", dataType = "float", name = "output01")

    node_C = nodeGraph.addNode(nodeName = "node_C")
    node_C_input01 = node_C.addPort(portType = "IN", dataType = "float", name = "input01").setValue(13)
    node_C_output01 = node_C.addPort(portType = "OUT", dataType = "float", name = "output01")

    node_D = nodeGraph.addNode(nodeName = "node_D")
    node_D_input01 = node_D.addPort(portType = "IN", dataType = "float", name = "input01")
    node_D_input02 = node_D.addPort(portType = "IN", dataType = "float", name = "input02")
    node_D_input03 = node_D.addPort(portType = "IN", dataType = "float", name = "input03")
    node_D_output01 = node_D.addPort(portType = "OUT", dataType = "float", name = "output01")

    node_E = nodeGraph.addNode(nodeName = "node_E")
    node_E_input01 = node_E.addPort(portType = "IN", dataType = "float", name = "input01").setValue(5)
    node_E_output01 = node_E.addPort(portType = "OUT", dataType = "float", name = "output01")

    node_F = nodeGraph.addNode(nodeName = "node_F")
    node_F_input01 = node_F.addPort(portType = "IN", dataType = "float", name = "input01")
    node_F_input02 = node_F.addPort(portType = "IN", dataType = "float", name = "input02")
    node_F_output01 = node_F.addPort(portType = "OUT", dataType = "float", name = "output01")

    #Connect nodes
    node_A_output01.connect(port = node_D_input01)
    node_B_output01.connect(port = node_D_input02)
    node_C_output01.connect(port = node_D_input03)
    node_E_output01.connect(port = node_F_input01)
    node_D_output01.connect(port = node_F_input02)

    #Set current node
    nodeGraph.setCurrentNode(node = node_F) 

    #remove connection
    # node_A_output01.removeConnection()

    #Run nodeGraph
    nodeGraph.start(node = nodeGraph.getCurrentNode())
 
    # app.cleanupUpstream(node = node_A)
    # A_in_1.setValue(4)
    # app.runNode(node = app.getCurrentNode())


if __name__ == "__main__":
    # import sys
    # packages = ["PyFBP"]
    # for i in sys.modules.keys():
    #     for package in packages:
    #         if i.startswith(package):
    #             print i
    main()
    



"""
TRASH
"""

"""
node_A = app.addNode(nodeName = "node_A")
A_in_1 = node_A.addPort(portType = "IN", dataType = "float", name = "In_01")
A_in_1.setValue(3)
A_out_1 = node_A.addPort(portType = "OUT", dataType = "float", name = "Out_01")

node_B = app.addNode(nodeName = "node_B")
B_in_1 = node_B.addPort(portType = "IN", dataType = "float", name = "In_01").setValue(1)
B_out_1 = node_B.addPort(portType = "OUT", dataType = "float", name = "Out_01")

node_C = app.addNode(nodeName = "node_C")
C_in_1 = node_C.addPort(portType = "IN", dataType = "float", name = "In_01").setValue(5)
C_out_1 = node_C.addPort(portType = "OUT", dataType = "float", name = "Out_01")

node_D = app.addNode(nodeName = "node_D")
D_in_1 = node_D.addPort(portType = "IN", dataType = "float", name = "In_01")
D_in_2 = node_D.addPort(portType = "IN", dataType = "float", name = "In_02")
D_out_1 = node_D.addPort(portType = "OUT", dataType = "float", name = "Out_01")

node_E = app.addNode(nodeName = "node_E")
E_in_1 = node_E.addPort(portType = "IN", dataType = "float", name = "In_01")
E_in_2 = node_E.addPort(portType = "IN", dataType = "float", name = "In_02")
E_out_1 = node_E.addPort(portType = "OUT", dataType = "float", name = "Out_01")

node_F = app.addNode(nodeName = "node_F")
F_in_1 = node_F.addPort(portType = "IN", dataType = "float", name = "In_01").setValue(7)
F_out_1 = node_F.addPort(portType = "OUT", dataType = "float", name = "Out_01")

node_G = app.addNode(nodeName = "node_G")
G_in_1 = node_G.addPort(portType = "IN", dataType = "float", name = "In_01").setValue(1)
G_out_1 = node_G.addPort(portType = "OUT", dataType = "float", name = "Out_01")

node_H = app.addNode(nodeName = "node_H")
H_in_1 = node_H.addPort(portType = "IN", dataType = "float", name = "In_01")
H_in_2 = node_H.addPort(portType = "IN", dataType = "float", name = "In_02")
H_in_3 = node_H.addPort(portType = "IN", dataType = "float", name = "In_03")
H_out_1 = node_H.addPort(portType = "OUT", dataType = "float", name = "Out_01")

loop_01 = Loop(count = 3)

A_out_1.connect(port = D_in_1)
B_out_1.connect(port = D_in_2)
C_out_1.connect(port = E_in_1)
D_out_1.connect(port = E_in_2)
E_out_1.connect(port = loop_01.getStartInput())
loop_01.getStartOutput().connect(port = H_in_1)
F_out_1.connect(port = H_in_2)
G_out_1.connect(port = H_in_3)
H_out_1.connect(port = loop_01.getEndInput())


# #create composition
comp_A = Subnet()
selectedNodes = [node_D, node_E, node_C]
for i in selectedNodes:
    comp_A.includeNode(i)
comp_A.build()

# # ===============================
app.setCurrentNode(node = loop_01.getEnd()) #set as current
app.runNode(node = app.getCurrentNode())

"""
