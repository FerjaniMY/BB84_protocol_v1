
from cqc.pythonLib import CQCConnection, qubit
import numpy as np
#import BitVector
"""
BB84 protocol description:
Protocol 1 — BB84 QKD (no noise). Outputs k ∈ {0,1}
`
to both Alice and Bob. Alice and
Bob execute the following:
1. For a small real-valued parameter η  1, and a large integer n  1, Alice chooses a string
x = x1,..., xN ∈ {0,1}
N uniformly at random where N = (4+η)n. She also chooses a
basis string θ = θ1,...,θN uniformly at random. She sends to Bob each bit xj by encoding
it in a quantum state according to the basis θj
: H
θj
|xji.
2. Bob chooses a basis string θ˜ = θ˜
1,...,θ˜
N uniformly at random. He measures qubit j in
the basis θ˜
j
to obtain outcome ˜xj
. This gives him a string ˜x = x˜1,..., x˜N.
3. Bob tells Alice over the CAC that he has received and measured all the qubits.
4. Alice and Bob tell each other over the CAC their basis strings θ and θ˜ respectively.
5. Alice and Bob discard all rounds j in which they didn’t measure in the same basis. Let
S = { j|θj = θ˜
j} denote the indices of the rounds in which they measured in the same
basis. Since Alice and Bob chose θ,θ˜ at random, for large values of n, they throw away
roughly N/2 ≈ 2n bits.
6. Alice picks a random subseta T ⊆ S for testing and tells Bob T over the CAC. That is,
Alice and Bob test roughly |T| ≈ N/4 ≈ n bits.
7. Alice and Bob announce xT and x˜T to each other over the CAC, where we denote by xT
the substring of x corresponding to the indices in the test set T. They compute the error
rate δ = W/|T|, where W = |{ j ∈ T | xj 6= x˜j}| is the number of errors when Alice and
Bob did measure in the same basis.
8. If the error rate δ 6= 0 , then Alice and Bob abort the protocol. Otherwise, they proceed to
denote xremain = xS\T and x˜remain = x˜S\T as the remaining bits, i.e., the bits where Alice
and Bob measured in the same basis, but which they did not use for testing. The length of
xremain and ˜xremain is approximately n bits.
9. Alice and Bob perform privacy amplification: Alice picks a random r, and computes
k = Ext(xremain,r). She sends r to Bob, who computes k = Ext(x˜remain,r).
aA random subset T of S is where each element in S is included in T with probability 1/2. By this definition, if
|S| is large, then |T| ≈ |S|/2

author :FerjaniMY
email:ferjanimedyassine@gmail.com

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
