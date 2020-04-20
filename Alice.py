from cqc.pythonLib import CQCConnection, qubit
import numpy as np
from BB84 import *
import time
import comm
from random import *


# Establish a connection  to  SimulaQron
with CQCConnection("Alice") as Alice:
 
 print("***********************BB84 protocol***************************")
 #Alice.closeClassicalServer() #if I want to use my socket functions
 m=[] 
 B=[]
 S=''
 n=30#number of qubits
 Alice.sendClassical("Bob",n)#send the number of qubits
 key= np.random.randint(0, high=2**n)#to replace with QRNG() function
 k=np.binary_repr(key,n) #binary representation
 #print("Alice's random key",key)
 #print("Alice's binary key:",k)
 print("*********************************")
 for index, digit in enumerate(k):
    
  
  m.append(str(digit))
  s=prepare_qubits(Alice,"Bob",digit) #send BB84 states
  #receive a confirmation msg from Bob via the CAC
  B.append(s[1])
  S+=str(s[1])
 """
 #send Alice's basis to Bob 
 ff=S.encode()#conversion to byte
 Alice.sendClassical("Bob",ff)
 """

 #print('a basis',B)
 
 #received Bob's Basis
 x=Alice.recvClassical()
 B_basis=list(x.decode())
 #print("Bob basis received",B_basis)
 #print(B_basis.split(""))
 aa=sifted_key(B,B_basis,m)
 print("Alice sifted key",aa[0])

 
 listToStr ="["+','.join(map(str, aa[1]))+"]"
 ff=listToStr.encode()
 Alice.sendClassical("Bob",ff)

 #####################TEST N RANDOM BITS################################
 test_key=[]
 test=list(range(0,len(aa[0])))
 
 test_indices=sample(test,len(aa[0])//2)
 print(test_indices)
 for i in test_indices:
 	test_key.append(aa[0][i])
 print("Test KEY",test_key)
 msg1=comm.list_to_bytes(test_key)
 Alice.sendClassical('Bob',msg1)
 time.sleep(1)
 test2=''
 
 msg2=comm.list_to_bytes(test_indices)
 Alice.sendClassical('Bob',msg2)

 #################### OTHER RECONCILIATION##########################

 #Later Alice will xor two from list indices, send indices and xor result to Bob
 """
 x=0
 f or i,j in enumerate(test_indices):
	x=(sifted_key[j]+sifted_key[j+1])%2
	print("positions",j)
	print("Xor result",x)
	del test_indices[0]
	del test_indices[1]

 #send(i,i+1),xor result  --> Send a -dict{tuple:XOR_value} , tuple(pos1,pos2)
 """
	
 #######################Seed################################################

 randBinList = lambda n: [randint(0,1) for b in range(1,n+1)] 
 kl=len(aa[0])#len of sifted key
 L=randBinList(kl)
 sifted_key=[]
 for i in aa[0]:
 	sifted_key.append(int(i))
 #print(sifted_key)
 #print(L)
 
 pk=comm.list_to_bytes(L)
 Alice.sendClassical("Bob",pk)


 private_key=np.dot(sifted_key,L)
 print("Alice private key :",private_key) 
 f = open("A_key.txt", "a")
 f.write(str(private_key))
 f.close()
 #Close  connection  to  SimulaQron
Alice.close()


 

 



 

 
