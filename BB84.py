
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

def sifted_key(A_basis,B_basis,key): 
 correct_basis=[]
 sifted_key=''

 for i in range(len(A_basis)):
  if A_basis[i]==B_basis[i]:
    correct_basis.append(i)
    sifted_key+=str(key[i])
  else:
    pass 
 return sifted_key,correct_basis

#def QRNG() Quantum Random number generator   
