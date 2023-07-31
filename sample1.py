import numpy as np


A = [4,1,11,10]
sA = [6,9,11,11]
eA =[0,-1,1,1]

n=len(A)
q=13

print (A,sA,eA)

xN_1 = [1] + [0] * (n-1) + [1]

print (xN_1)
A = np.floor(np.polydiv(A,xN_1)[1])

bA = np.polymul(A,sA)%q
bA = np.floor(np.polydiv(bA,xN_1)[1])

bA = np.polyadd(bA,eA)%q
bA = np.floor(np.polydiv(bA,xN_1)[1])
print ("Print output\n",bA)
