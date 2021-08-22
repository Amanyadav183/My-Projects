import matplotlib.pyplot as mp
X=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
Y=[5,4,3,2,1,0,1,2,3,4,5]

P=[-6,-8,-7,-7,-6,-8]
Q=[0,0,0,7,7,7]

C=[6,6,7,8,8,7,6]
D=[0,7,7,7,4,4,4]

S=[9,10,10,10,11]
T=[7,4,0,4,7]

H=[12,13,13,13,14]
G=[7,7,0,7,7]

M=[15,15,15,16,17,17,17]
N=[0,7,3.5,3.5,3.5,0,7]

J=[18,18,20,20,18]
K=[0,7,7,0,0]

I=[21,21,23,23]
R=[0,7,0,7]

A=[-5,-4.5,-4,-3,-2.5,-2,-1,-0.5,0,0.5,1,2,2.5,3,4,4.5,5]
B=[5,6,6.5,7,7,7,6.5,6,5,6,6.5,7,7,7,6.5,6,5]

mp.plot(X,Y,linewidth=8)
mp.plot(A,B,linewidth=8)
mp.plot(P,Q,linewidth=8)
mp.plot(C,D,linewidth=8)
mp.plot(S,T,linewidth=8)
mp.plot(H,G,linewidth=8)
mp.plot(M,N,linewidth=8)
mp.plot(J,K,linewidth=8)
mp.plot(I,R,linewidth=8)
mp.title("#I Love Python")
mp.show()
