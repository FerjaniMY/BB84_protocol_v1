from cqc.pythonLib import CQCConnection, qubit
import numpy as np
from BB84 import *
import time
import comm
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
 #print("bob's initial key :",key)
 ff=B.encode()#conversion to byte
 Bob.sendClassical("Alice",ff)
 
 #receive Alice's basis
 msg=Bob.recvClassical()

 res =comm.bytes_to_list(msg)
 #print("Alice's Basis received",res)
 key_s=''
 
 for c in res:
  key_s+=str(key[c])
  
 print("Bob sifted key",key_s)
 
 time.sleep(1)
 msg1=Bob.recvClassical()
 tested_key_A=comm.bytes_to_list(msg1)
 #print("Alice's tested key received",tested_key_A)
 time.sleep(1)
 msg2=Bob.recvClassical()
 test_indices_A=comm.bytes_to_list(msg2)#test_indices from Alice

 #print("Test indices received",test_indices_A)
  
 test_key_B='' 
 for i in test_indices_A:
  test_key_B+=key_s[i]
  
 print("Bob tested key",test_key_B) 
 ########################"Error Rate in tested keys####################################################
 x=0
 for i in range(len(test_key_B)):
 	if test_key_B[i]!=tested_key_A[i]:
 	 x+=1
 
 error_rate=x/len(test_key_B)
  
 print("Error rate in tested bits: {}% .".format(error_rate))

 ###################Privacy Amplification#####################################
 sifted_key=[]
 pk=Bob.recvClassical()
 L=comm.bytes_to_list(pk)
 for i in key_s:
 	sifted_key.append(int(i))
 private_key=np.dot(sifted_key,L)#key_s is the sifted key
 print("Bob private key :",private_key) 
 f = open("B_key.txt", "a")
 f.write(str(private_key))
 f.close()


 #############################################################################
 
 
 Bob.close()

