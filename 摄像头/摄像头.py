import math
def changepoint(P=[]):
if P[1]>0 :
P[1]=math.sqrt((P[1]*P[1]+P[0]*P[0])/(math.cos(P[2])*math.cos(P[2]))-P[0]*P[0])
else:
P[1]=(-1)*math.sqrt((P[1]*P[1]+P[0]*P[0])/(math.cos(P[2])*math.cos(P[2]))-P[0]*P[0])
return P

def lenth(P=[],L=[]):
l=math.sqrt((P[0]-L[0])(P[0]-L[0])+(P[1]-L[1])(P[1]-L[1]))
return l
def reallength (l,L=[]):
a=L[3]*l/(math.cos(L[2])*L[4])
return a

L=[0.075,9.91/24641080,0.785,1000,3.09]#横坐标，纵坐标，角度，高度，焦距
P=[7.285,12.12/2464108,0.785,1000,3.09]
changepoint(L)
changepoint(P)
l=lenth(L,P)*0.165
a=reallength(l,L)
print(a)


