import numpy as np
import sys

q=13

A=np.array([[4 ,1, 11, 10],[5, 5 ,9 ,5],[3, 9 ,0 ,10],[1, 3 ,3 ,2],[12, 7 ,3 ,4],[6, 5 ,11 ,4],[3, 3, 5, 0]])

sA = np.array([[6],[9],[11],[11]])
eA = np.array([[0],[-1],[1],[1],[1],[0],[-1]])

bA = np.matmul(A,sA)%q
print (bA)

bA = np.add(bA,eA)%q
print
print ("Print output\n",bA)
