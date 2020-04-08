from cqc.pythonLib import CQCConnection, qubit
import numpy as np
from BB84 import *
from CAC.classical_comm import *

# Establish a connection  to  SimulaQron
with CQCConnection("Alice") as Alice:
 
 print("***********************BB84 protocol***************************")
 #Alice.closeClassicalServer()
 m=[] 
 B=[]
 S=''
 n=20#number of qubits
 Alice.sendClassical("Bob",n)#send the number of qubits
 key= np.random.randint(0, high=2**n)#to replace with QRNG() function
 k=np.binary_repr(key,n) #binary representation
 print("Alice's random key",key)
 print("Alice's binary key:",k)
 print("*********************************")
 for index, digit in enumerate(k):
    
  
  m.append(str(digit))
  s=prepare_qubits(Alice,"Eve",digit) #send BB84 states
  #receive a confirmation msg from Bob via the CAC
  B.append(s[1])
  S+=str(s[1])
 """
 #send Alice's basis to Bob 
 ff=S.encode()#conversion to byte
 Alice.sendClassical("Bob",ff)
 """

 print('a basis',B)
 
 #received Bob's Basis
 x=Alice.recvClassical()
 B_basis=list(x.decode())
 #print("Bob basis received",B_basis)
 #print(B_basis.split(""))
 aa=raw_key(B,B_basis,m)
 print("Alice raw key",aa[0])
 #R_ext = [random.randint(0, 1) for a in range(0, len(aa[0]))]
 pairs = random.sample(aa[0],len(aa[0])/2)
 print("Seed fqdkl,",pairs)
 
 #print('Bobs basis received//////',d)
 #Check matching basis
 #extract raw key
 #priv_amp(Alice,"Bob",m)
 #test randomly some indices
 #error rate
 #decision abort or confirm protocol
 
 listToStr ="["+','.join(map(str, aa[1]))+"]"
 ff=listToStr.encode()
 Alice.sendClassical("Bob",ff)
 
 #receive_message(Alice)
 #print("priv amp",pv)
 #Close  connection  to  SimulaQron
 Alice.close()


 

 
