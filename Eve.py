from cqc.pythonLib import CQCConnection, qubit
import numpy as np
from BB84 import *
# Establish a connection  to  SimulaQron
with CQCConnection("Eve") as Eve:
 B=[]
 n=18
 key=[]
 for i in range(n):
  c=receive_qubits(Eve)
  #print("out meas.",c[0])
  key.append(c[0])
  B.append(c[1])
 print("Eve's Key :",key)
 print("Eve's Basis :",B)
 for x in key:  
  s=prepare_qubits(Eve,"Bob",x)



 # Close  connection  to  SimulaQron
 Eve.close()
