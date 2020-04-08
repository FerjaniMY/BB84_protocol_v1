
"""
BB84 protocol
author :FerjaniMY
email:ferjanimedyassine@gmail.com

"""


from cqc.pythonLib import CQCConnection, qubit
import numpy as np
import random

def prepare_qubits(Sender,receiver,key_bit):
   
   q=qubit(Sender)
   S_basis="" # The sender basis

   if key_bit =='1':  #prepare qubits in |1> state
    q.X() #apply X gate
   
   # convert  to  Hadamard  basis randomly
   if 0.5 < np.random.random(): 
    q.H() #apply hadamard gate
    S_basis='H'
   else:
    S_basis='S'
   
   Sender.sendQubit(q,receiver)

   return [q,S_basis]

def receive_qubits(Receiver):
  #R_basis=[] #Receiver basis
  # Wait to  receive a qubit
  q=Receiver.recvQubit()
  C="" # for basis choice
  # If we  chose  the  Hadamard  basis
  # to  measure in, apply H
  if 0.5 < np.random.random(): 
   q.H()
   C='H'
  else:
   C='S' #S: Standard Basis
  
  m=q.measure()
   
  # Measure  the  qubit  in the  standard
  # basis  and  store  the  outcome  in m
  
  return [m,C]

def raw_key(A_basis,B_basis,key): 
 correct_basis=[]
 raw_key=[]

 for i in range(len(A_basis)):
  if A_basis[i]==B_basis[i]:
    correct_basis.append(i)
    raw_key.append(key[i])
  else:
    pass 
 return raw_key,correct_basis
 
#def reconciliation(keyA,keyB):
 




"""
def error_rate(keyA,keyB):
 s=0 
 for i in range(keyA): 
  if keyA[i]!=keyB[i]:
   s+=1
 e=s/len(keyA)
 return e


def check_basis(A_basis,B_basis):
 correct_basis=[]
 discarded=[]
 for i,b in enumerate(zip(A_basis,B_basis)):
   if b[0]==b[1]
    correct_basis.append(i)
   else:
    discarded.append(i)
 return correct_basis,discarded
def check_errors(self, test_bits, peer_test_bits):
        number_of_errors = len([i for i in range(len(test_bits)) if test_bits[i] != peer_test_bits[i]])
        delta = number_of_errors/len(test_bits)

def priv_amp(sender,receiver,k): #key=list
 
 l=[]
 
 #x=random.sample(k, 2)#Choose randomly two bit of the key
 i=random.randint(0,len(k)-1)
 j=random.randint(0,len(k)-1) 
 while(len(k)!=0):
  if i!=j:
   x=int(k[i])
   del k[i] #delete
   y=int(k[j])
   del k[i]
   xor=(x+y)%2
   inf=[i,j,xor]
   l.append(inf)
   sender.sendClassical(receiver,inf) #send two positions and their xor
  
# return l
"""
#def reconciliation
#def error_correction
#def detect_Eve
#def QRNG() Quantum Random number generator   
