from cqc.pythonLib import CQCConnection, qubit
import numpy as np
from BB84 import *
from CAC.classical_comm import *
import ast

# Establish  connection  to  SimulaQron
with CQCConnection("Bob") as Bob:
 #Bob.closeClassicalServer() #if I want to use my socket functions
 n=Bob.recvClassical()[0] #number of qubits given by Bob ("Eve")
 key=[]
 B=''
 for i in range(0,n):
  c=receive_qubits(Bob)
  #send confirmation to Alice via CAC
  #print("out meas.",c[0])
  key.append(c[0])
  B+=str(c[1]) #Bob basis
 

 #send Basis to Alice
 print("bob's initial key :",key)
 ff=B.encode()#conversion to byte
 Bob.sendClassical("Alice",ff)
 
 #receive Alice's basis
 a=Bob.recvClassical()
 x=a.decode()
 res = ast.literal_eval(x)
 #print("Alice's Basis received",res)
 key_s=[]
 
 for c in res:
  key_s.append(key[c])
  
 print("Bob final raw key",key_s)

 #check matching basis
 #print("Bob's key :",key)
 #d=Bob.recvClassical()[0]
 #print("pri amp::::::",d)
 #raw key
 #test randomly some indices
 #error rate
 #decision abort or confirm protocol

 #send_message(Bob, "Alice",B)
 
 Bob.close()

