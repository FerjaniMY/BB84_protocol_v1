
from cqc.pythonLib import CQCConnection, qubit
import numpy as np
"""
BB84 protocol 
"""

def prepare_qubits(Sender,receiver,key_bit):
   
   q=qubit(Sender)
   S_basis="" # The sender basis

   if key_bit == 1:  #prepare qubits in |1> state
    q.X() #apply X gate
   else:
    pass
   # convert  to  Hadamard  basis randomly
   if 0.5 < np.random.random(): 
    q.H() #apply hadamard gate
    S_basis='H'
   else:
    S_basis='S'
    pass
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
   pass
  # Measure  the  qubit  in the  standard
  # basis  and  store  the  outcome  in m
  m=q.measure ()
  return [m,C]

def check_basis(A_basis,B_basis):
 correct_basis=[]
 discarded=[]
 
 for i in A_basis:
  for j in B_basis:
   if i==j:
    correct_basis.append(i)
   else:
    discarded.append(i)
 return correct_basis,discarded

#def privacy_amplification(key): #key : list
#def detect_Eve
#def QRNG() Quantum Random number generator   
