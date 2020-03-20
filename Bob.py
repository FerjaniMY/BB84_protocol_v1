from cqc.pythonLib import CQCConnection, qubit
import numpy as np
from BB84 import *
# Establish  connection  to  SimulaQron
with CQCConnection("Bob") as Bob:
 
 n=18
 key=[]
 B=[]
 for i in range(n):
  c=receive_qubits(Bob)
  #print("out meas.",c[0])
  key.append(c[0])
  B.append(c[1])
 print("Bob's Basis :",B)
 print("Bob's key :",key)
 Bob.close()
