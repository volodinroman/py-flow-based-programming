
import sys
import os

project_root  = os.path.dirname(os.path.abspath(__file__))
project_nodes = os.path.join(project_root, "nodes")

sys.path.append(project_root)
sys.path.append(project_nodes)


