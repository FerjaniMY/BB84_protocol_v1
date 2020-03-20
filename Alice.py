from cqc.pythonLib import CQCConnection, qubit
import numpy as np
from BB84 import *
# Establish a connection  to  SimulaQron
with CQCConnection("Alice") as Alice:
 
 B=[]
 n=18 #number of qubits
 key= np.random.randint(0, high=2**n)#to replace with QRNG() function
 k=np.binary_repr(key,n) #binary representation
 print("Alice's random key",key)
 print("Alice's binary key:",k)
 for x in k:
 
  s=prepare_qubits(Alice,"Eve",x)

  B.append(s[1])
 print("Alice's basis : ",B)
 # Close  connection  to  SimulaQron
 Alice.close()


 
